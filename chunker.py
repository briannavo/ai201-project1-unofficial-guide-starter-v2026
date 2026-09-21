"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

import re
from dataclasses import dataclass

import config
from ingest import Document


@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


# The blank line between a thread's title and each of its replies, and the
# sentence end we fall back to when a single reply is somehow over budget.
_PARAGRAPH_BREAK = re.compile(r"\n\s*\n")
_SENTENCE_END = re.compile(r"(?<=[.!?])\s+")

# Every document in advice_threads opens with a line like
# "THREAD: How much laptop do I actually need for CS courses?"
_TITLE_PREFIX = "THREAD:"


def _blocks(text: str, limit: int) -> list[str]:
    """
    Break one document into the units this chunker refuses to cut through.

    For advice_threads that's the title line and each individual reply, since
    they're separated by blank lines. A block longer than `limit` on its own
    gets broken at sentence ends instead — a chunk over budget is worse than a
    long reply split in two.
    """
    units: list[str] = []

    for block in _PARAGRAPH_BREAK.split(text):
        block = block.strip()
        if not block:
            continue

        if len(block) <= limit:
            units.append(block)
            continue

        sentence = ""
        for part in _SENTENCE_END.split(block):
            if sentence and len(sentence) + 1 + len(part) > limit:
                units.append(sentence)
                sentence = part
            else:
                sentence = f"{sentence} {part}".strip()
        if sentence:
            units.append(sentence)

    return units


def _joined_length(blocks: list[str]) -> int:
    """How long these blocks will be once joined with blank lines."""
    if not blocks:
        return 0
    return sum(len(b) for b in blocks) + 2 * (len(blocks) - 1)


def split_documents(documents: list[Document]) -> list[Chunk]:
    """
    Fill chunks up to config.CHUNK_SIZE characters with whole replies.

    The strategy, and why:

    Every thread in this corpus runs 327-812 characters, and each reply inside
    it runs roughly 100-200. A fixed 800-character window therefore does almost
    nothing here — 22 of the 23 threads come back uncut — and a hard cut at any
    smaller number lands in the middle of somebody's sentence, which produces
    the fragment the brief warns about.

    So 550 is a budget, not a blade. This walks a thread reply by reply and
    keeps adding replies to the current chunk until the next one would push it
    past the budget. Chunks come out under 550 characters and never split a
    reply down the middle.

    Two details that matter for retrieval:

      - The "THREAD: ..." title rides along on every chunk from that thread.
        It costs ~60 characters and means a chunk taken from halfway down the
        thread still says which question it is answering.
      - Overlap is one whole reply, not config.CHUNK_OVERLAP characters. The
        last reply of a chunk repeats as the first reply of the next, so an
        answer that depends on two neighbouring replies can still be found in
        one chunk. (CHUNK_OVERLAP still applies to fallback_split.)
    """
    chunk_size = config.CHUNK_SIZE
    chunks: list[Chunk] = []

    for doc in documents:
        blocks = _blocks(doc.text, chunk_size)
        if not blocks:
            continue

        # Pull the title off the front so it can be repeated on every chunk.
        header = blocks[0] if blocks[0].startswith(_TITLE_PREFIX) else ""
        body = blocks[1:] if header else blocks
        if not body:
            # A document that is nothing but a title. Keep it as it is.
            body, header = [blocks[0]], ""

        # The title eats into the budget, so the replies get what's left.
        budget = chunk_size - (len(header) + 2 if header else 0)

        def emit(buffer: list[str], index: int) -> None:
            parts = [header, *buffer] if header else buffer
            chunks.append(
                Chunk(
                    text="\n\n".join(parts),
                    source=doc.source,
                    index=index,
                    produced_by="chunker.py::split_documents",
                )
            )

        buffer: list[str] = []
        index = 0
        for block in body:
            if buffer and _joined_length(buffer) + 2 + len(block) > budget:
                emit(buffer, index)
                index += 1
                # Carry the last reply forward as overlap, but only if the
                # next one still fits beside it.
                tail = buffer[-1]
                buffer = [tail] if len(tail) + 2 + len(block) <= budget else []
            buffer.append(block)

        if buffer:
            emit(buffer, index)

    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
