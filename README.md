# The Unofficial Guide

<!-- Replace this line with your name and which corpus you picked. -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     Milestone 5. -->

## Chunking Strategy

**Chunk size: 550 characters**
**Overlap: One whole reply**

<!-- What about YOUR documents made you pick these numbers? Short posts and
     long sectioned guides don't want the same chunking, and "800 seemed
     reasonable" earns nothing. Point at something you noticed when you read
     the documents in Milestone 1.

     If you changed your mind partway through, say so and say why. That's worth
     more than pretending you got it right first time.

     Milestone 3. -->

550 characters fits enough for the title (question/topic) and 2-3 replies, which is the smallest amount in this corpus that contains an answer and not only a single user's opinion. The overlap is one whole reply as in some threads some users disagree or say differing things, so we don't want rebuttals separated from what it is rebutting

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

Chunk 1  |  source: thread_bike_commute.txt#0  |  produced by: chunker.py::split_documents

THREAD: Is a bike worth it for a 20 minute walk commute?

--- reply 1 (14 votes) ---
Yeah. Cuts an 18 minute walk to about 6. The thing nobody mentions is storage — covered bike parking exists at three buildings and is full by 9am at all three.

--- reply 2 (9 votes) ---
Counterpoint, I sold mine. Between November and March the paths are either icy or salted and salt destroys a drivetrain in one season.

Chunk 2  |  source: thread_commuting.txt#1  |  produced by: chunker.py::split_documents

THREAD: Commuting an hour each way — is it survivable?

--- reply 3 (13 votes) ---
Watch the evening bus timetable before you register for anything that ends after 6pm.

--- reply 4 (17 votes) ---
I commuted for two years. The thing that made it work was treating the train as study time rather than dead time.

Chunk 3  |  source: thread_internship_timing.txt#0  |  produced by: chunker.py::split_documents

THREAD: When should I start looking for a summer internship?

--- reply 1 (30 votes) ---
Earlier than feels reasonable. Large employers close applications in October and November for the following summer.

--- reply 2 (25 votes) ---
Smaller and local places hire in February and March, so if you missed autumn you have not missed everything.

--- reply 3 (19 votes) ---
The careers office reviews CVs on a drop-in basis and the queue is almost never longer than one person.

Chunk 4  |  source: thread_office_hours_etiquette.txt#0  |  produced by: chunker.py::split_documents

THREAD: Is it weird to go to office hours with no specific question?

--- reply 1 (44 votes) ---
No, and this is the single most common thing first years get wrong. 'I'm following the lectures but I don't feel like I understand the shape of it' is a completely normal thing to say.

--- reply 2 (29 votes) ---
They're usually empty. You are doing the instructor a favour by turning up.

--- reply 3 (18 votes) ---
If it helps, treat it as a standing appointment. Go every week for a month and it stops feeling like a thing.

Chunk 5  |  source: thread_roommate_conflict.txt#0  |  produced by: chunker.py::split_documents

THREAD: Roommate situation isn't working. What now?

--- reply 1 (28 votes) ---
Talk to your RA early, and frame it as 'we need help sorting this out' rather than 'move me'. Room changes are possible butthe process starts with mediation and skipping that step slows it down.

--- reply 2 (14 votes) ---
Room changes happen at the semester boundary almost always, and mid-semester only in fairly serious cases.

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question: Does it matter if I sleep late?**

**Yes, fixing your sleep schedule does matter, and one helpful strategy is scheduling no classes before 10 AM rather than trying to become a morning person (thread_sleep_schedule.txt). Additionally, the library being open until 2 AM is considered a trap rather than a schedule (thread_sleep_schedule.txt).

Sources retrieved: thread_commuting.txt, thread_late_work.txt, thread_sleep_sched**

```
```

**My relevance cutoff: 0.70**

I ran 5 questions that my corpus covers and 5 that aren't. I found that 0.6 was slightly too low to cover all of the best distances for in corpus questions, so I raised it to 0.70. The gap between in-scope and out of scope distances was from 0.619-0.787 so this cutoff is enough to keep out of corpus answers out, while not cutting out correct answers that are slightly further than 0.6.

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

| Question | In corpus? | Best distance |
| --- | --- | --- |
| How should I handle a bad roommate situation? | Yes | 0.3745 |
| What should my laptop specs be for CS major? | Yes | 0.3087 |
| Should I email my professor about an issue I am having? | Yes | 0.6188 |
| Can I go to office hours without questions? | Yes | 0.4886 |
| Does it matter if I sleep late? | Yes | 0.6048 |
| What is the capital of Mongolia? | No | 0.8902 |
| How do I change the oil in a diesel engine? | No | 0.9299 |
| Who won the 1994 World Cup? | No | 0.7866 |
| What is the recommended dosage of ibuprofen for a headache? | No | 0.8280 |
| How do I write a for loop in Rust? | No | 0.8712 |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1. I asked Claude to help me write the chunking function from my notes. It gave me a recommended chunk size, but ignored overlap, so I prompted it with further information on overlap.**

**2. I asked Claude to help me brainstorm the best cutoff given the distances for each test question. It gave me 0.70 which was close to my idea, but provided no strong evidence for why. I prompted Claude to explain why 0.70 so that I could more confidently decide on a cutoff.**

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | pass | pass | pass | MET |
| 2. Every answer names a source | 5 of 5 | pass | pass | pass | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | pass | pass | pass | MET |
| 4. Each answer should only require about 1-2 chunks.| 5 of 5 | pass | pass | pass | MET |
| 5. | The answer should take comment votes into account, with more votes having more weight in the final answer. | 5 of 5 | fail | fail | fail | MISSED |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

File: results\run_2026-09-23_2052.md
Function: py run_eval.py

### For my math class, does the edition of my math textbook matter? — run 1

- Best distance: 0.4988 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_printing.txt, thread_textbook_editions.txt

```
For math, the edition almost never matters; only the problem numbering shifts. 

Source: `thread_textbook_editions.txt`
```

### For my math class, does the edition of my math textbook matter? — run 2

- Best distance: 0.4988 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_printing.txt, thread_textbook_editions.txt

```
For a math class, the edition of the textbook almost never matters, as only the problem numbering shifts. 

Source: `thread_textbook_editions.txt`
```

### For my math class, does the edition of my math textbook matter? — run 3

- Best distance: 0.4988 (passed the gate)
- Sources retrieved: thread_first_gen.txt, thread_printing.txt, thread_textbook_editions.txt

```
For math, the edition almost never matters; only the problem numbering shifts. 

Source: thread_textbook_editions.txt
```

### Is 16GB of RAM enough for my laptop as a CS major? — run 1

- Best distance: 0.2290 (passed the gate)
- Sources retrieved: thread_laptop_specs.txt, thread_pass_fail.txt, thread_printing.txt

```
Yes, 16GB of RAM is recommended as the number worth paying for, with users noting that 8GB can struggle by the final project (thread_laptop_specs.txt).
```

### Is 16GB of RAM enough for my laptop as a CS major? — run 2

- Best distance: 0.2290 (passed the gate)
- Sources retrieved: thread_laptop_specs.txt, thread_pass_fail.txt, thread_printing.txt

```
Yes, 16GB of RAM is enough and is the one number worth paying for. 

Source: thread_laptop_specs.txt
```

### Is 16GB of RAM enough for my laptop as a CS major? — run 3

- Best distance: 0.2290 (passed the gate)
- Sources retrieved: thread_laptop_specs.txt, thread_pass_fail.txt, thread_printing.txt

```
Yes, 16GB of RAM is enough and is the one number worth paying for. 

Source: thread_laptop_specs.txt
```

### Is it better to be involved in a lot of clubs or focus on only a few clubs? — run 1

- Best distance: 0.5077 (passed the gate)
- Sources retrieved: thread_clubs.txt, thread_first_gen.txt, thread_study_spots.txt

```
It is better to focus on a few clubs rather than breadth across many, because depth in one club is worth more if you want a leadership position later. (Source: thread_clubs.txt)
```

### Is it better to be involved in a lot of clubs or focus on only a few clubs? — run 2

- Best distance: 0.5077 (passed the gate)
- Sources retrieved: thread_clubs.txt, thread_first_gen.txt, thread_study_spots.txt

```
It is better to focus on a few clubs. According to *thread_clubs.txt*, depth in one club is worth more for future leadership positions than breadth across five.
```

### Is it better to be involved in a lot of clubs or focus on only a few clubs? — run 3

- Best distance: 0.5077 (passed the gate)
- Sources retrieved: thread_clubs.txt, thread_first_gen.txt, thread_study_spots.txt

```
According to `thread_clubs.txt`, depth in one club is worth more than breadth across five if you want a leadership position later. Additionally, reply 1 states that "Two you actually turn up to beats six you signed up for at the fair."
```

### Can I go to office hours without questions? — run 1

- Best distance: 0.4886 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_office_hours_etiquette.txt, thread_professor_email.txt

```
Yes, you can go to office hours without a specific question. As one reply notes, saying something like "I'm following the lectures but I don't feel like I understand the shape of it" is completely normal (thread_office_hours_etiquette.txt).
```

### Can I go to office hours without questions? — run 2

- Best distance: 0.4886 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_office_hours_etiquette.txt, thread_professor_email.txt

```
Yes, it is completely normal to go to office hours without a specific question, such as saying you don't feel like you understand the shape of the lectures (*thread_office_hours_etiquette.txt*). Additionally, office hours are usually empty, so you are actually doing the instructor a favor by showing up (*thread_office_hours_etiquette.txt* and *thread_professor_email.txt*).
```

### Can I go to office hours without questions? — run 3

- Best distance: 0.4886 (passed the gate)
- Sources retrieved: thread_first_year_regret.txt, thread_office_hours_etiquette.txt, thread_professor_email.txt

```
Yes, it is completely normal to go to office hours without a specific question, such as to say you are following the lectures but don't feel like you understand the shape of it (thread_office_hours_etiquette.txt). Additionally, office hours are usually empty, so attending them does the instructor a favor (thread_office_hours_etiquette.txt and thread_professor_email.txt).
```

### Does it matter if I sleep late? — run 1

- Best distance: 0.6048 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_late_work.txt, thread_sleep_schedule.txt

```
Yes, it matters, and a helpful strategy is to schedule no classes before 10am rather than trying to become a morning person (*thread_sleep_schedule.txt*).
```

### Does it matter if I sleep late? — run 2

- Best distance: 0.6048 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_late_work.txt, thread_sleep_schedule.txt

```
Yes, fixing your sleep matters, and one helpful strategy is scheduling no classes before 10 AM rather than trying to become a morning person (thread_sleep_schedule.txt). Additionally, the library being open until 2 AM is a trap rather than a schedule to follow (thread_sleep_schedule.txt).
```

### Does it matter if I sleep late? — run 3

- Best distance: 0.6048 (passed the gate)
- Sources retrieved: thread_commuting.txt, thread_late_work.txt, thread_sleep_schedule.txt

```
Yes, fixing your sleep matters, and the most helpful approach may be scheduling no classes before 10am rather than trying to become a morning person (thread_sleep_schedule.txt).
```


## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| # | Criterion | Verdict | How I decided |
|---|---|---|---|
| 1 | For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer. | MET | Although not every run was consistent in pass/fail, each test question in all three runs retrieved the correct chunk that would contain the answer. |
| 2 | Every answer the system produces names at least one source document. | MET | Every answer that was provided in the test runs provided a source either in-text or after the answer with a "Source" tag. |
| 3 | When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries. | MET | All of my 5 test out-of-scope questions were refused in the 3 test runs because they did not meet the best distance cutoff that I set (0.7). This worked exactly as I wanted to and ensured that questions that my corpus could not actually answer weren't asked. |
| 4 | Each answer should only require about 1-2 chunks. | MET | All of my test questions in all three runs only source one to two chunks at most for the answer.  |
| 5 | The answer should take comment votes into account, with more votes having more weight in the final answer. | MISSED | This criteria couldn't be judged/measured properly as I never implemented the idea of replies having votes to the RAG system, thus it couldn't actually weight higher voted replies in the answer. |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

In my original run, I realized after checking my run results, question 1 fully failed and question 3 had mixed pass/fail because my questions and expectations were incorrect. I was asking questions that were too vague and/or my "expects" phrase was not something that would be said consistently. For example, in question 3 about whether it's better to be in a lot of clubs or a few clubs, I had the expected phrase be "a few clubs". However, one response that failed said depth is better than breadth, which is essentially the same thing but did not use the expects phrase. 

## The Improvement

**What I changed:** 

Question 1 to be: How many pass/fails do I get in one year?

Question 3 to be: How many pages does the $30 printing quota give you?

**Why I picked it:** 

Question 1 was too vague before and did not have a single direct answer from the corpus. I changed it to be much more specific and something that had one single correct answer from the corpus. Question 3 before was answered correct, but I incorrectly decided an expects phrase that wasn't realistic/would be repeated. I changed it to a question that is specific and has one direct answer.

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |
|---|---|---|---|---|---|
| 1. Retrieved chunk contains the answer | 4 of 5 | pass | pass | pass | MET |
| 2. Every answer names a source | 5 of 5 | pass | pass | pass | MET |
| 3. Gate stops out-of-corpus questions | 4 of 5 | pass | pass | pass | MET |
| 4. Each answer should only require about 1-2 chunks.| 5 of 5 | pass | pass | pass | MET |
| 5. | Source attribution for each answer should be correct and not merely present for at least 4 out of 5 test questions.| 4 of 5 | pass | pass | pass | MET |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

Yes, both changing my questions to be more specific and changing my 5th criteria worked. I know this because now my question tests are passing all 3 runs, and my 5th criteria is relevant, can be measured, and is passing for the new run.

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

     After my fixes, none of my criterion are missed.

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->

     Knowing what I know now, I would've rewritten my 5th criteria to begin with. It didn't make sense with the RAG system that we developed and could not be measured.
