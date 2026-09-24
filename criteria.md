# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. *"Retrieval works"* is an opinion. *"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"* is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; *"80% seemed reasonable"* does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer MET

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**
<!-- e.g. "One of my questions is about a topic only two documents mention, so
     I expect that one to be hard." -->
Some questions are harder to answer as some topics have users that say differing information, but at least 80% of the test questions should return chunks with the correct answer.

**Why was this met:**
Although not every run was consistent in pass/fail, each test question in all three runs retrieved the correct chunk that would contain the answer.
---


## 2. Every answer names a source MET

Every answer the system produces names at least one source document.

**Why this target:**
<!-- Why all five and not four? What about your setup makes that achievable —
     or what would have to go wrong for it not to be? -->
Every answer should name at least one source document so that the answer can be explainable. Without knowing where the answer comes from, we cannot fix errors that occur. Most topics only have one relevant thread so one document is enough.

**Why was this met:**
Every answer that was provided in the test runs provided a source either in-text or after the answer with a "Source" tag.
---

## 3. The relevance gate stops out-of-corpus questions MET

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**
<!-- What did your distances look like when you set the cutoff in Milestone 4?
     Was there a clean gap, or did the two groups overlap? -->
The system should not try to hallucinate an answer when encountering an out of context question, so setting the cutoff to be 4/5 tries ensures this while leaving some room for errors.

**Why was this met:**
All of my 5 test out-of-scope questions were refused in the 3 test runs because they did not meet the best distance cutoff that I set (0.7). This worked exactly as I wanted to and ensured that questions that my corpus could not actually answer weren't asked.
---

## 4. Something about your chunks MET

Each answer should only require about 1-2 chunks.

<!-- YOU WRITE THIS ONE.

     How would you know if your chunks were the right size? Name something
     countable or observable.

     Examples of the right shape — don't copy these, they should come from
     what you actually saw in Milestone 3:
       - "At least 4 of 5 sampled chunks read as a complete thought, with no
          sentence cut in half at either end."
       - "No chunk is shorter than 200 characters, since anything below that
          in my corpus turned out to be a heading with no content under it." -->



**Why this target:**
Each chunk contains one question and various replies to the question. The topics in the corpus widely vary so almost any question that could be asked to the system should be able to be answered by 1-2 specific chunks.

**Why was this met:**
All of my test questions in all three runs only source one to two chunks at most for the answer. 
---

## 5. Your choice MISSED

Original: The answer should take comment votes into account, with more votes having more weight in the final answer.

Revised: Source attribution for each answer should be correct and not merely present for at least 4 out of 5 test questions.

<!-- YOU WRITE THIS ONE TOO.

     Pick something you actually care about getting right. It could be about
     speed, about refusals, about a particular kind of question your corpus
     handles badly, about source attribution being correct rather than merely
     present — anything, as long as it names a number or an observable
     outcome. -->



**Why this target:**
Votes represent what other users considered to be the top answer to the thread, thus these replies should be weighted more heavily in the answer from the system.

**Why was this missed:**
This criteria couldn't be judged properly as I never implemented the idea of replies having votes to the RAG system, thus it couldn't actually weight higher voted replies in the answer. The new version is something that I can actually check using my evaluation results.
---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
