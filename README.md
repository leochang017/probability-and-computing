# Probability and Computing for Machine Learning and Finance

A year-long, self-taught, calculus-based probability course built on Blitzstein & Hwang's
*Introduction to Probability* and the Harvard Stat 110 lectures, followed by a short stretch
of statistics and regression from *OpenIntro Statistics* and a final project. The year is split
into 18 cycles. Each cycle has the same three deliverables: a written problem set (six textbook
exercises plus two quantitative-finance interview problems, mostly from Zhou's *A Practical Guide
to Quantitative Finance Interviews*), one short Python program that checks the chapter's main
result by brute-force simulation, and a half-page log. By the end there should be roughly 110
solved problems and 18 programs in this one place.

## Cycles

| Cycle | Chapter | Topic | Program | Status |
|------:|---------|-------|---------|--------|
| 1 | B&H ch. 1 | Probability and counting (birthday problem) | [cycle01/simulation.py](cycle01/simulation.py) | done |
| 2 | B&H ch. 2 | Conditional probability | [cycle02/simulation.py](cycle02/simulation.py) | upcoming |
| 3 | B&H ch. 3 | Random variables and their distributions | [cycle03/simulation.py](cycle03/simulation.py) | upcoming |
| 4 | B&H ch. 4 | Expectation | [cycle04/simulation.py](cycle04/simulation.py) | upcoming |
| 5 | B&H ch. 5 | Continuous random variables | [cycle05/simulation.py](cycle05/simulation.py) | upcoming |
| 6 | B&H ch. 6 | Moments | [cycle06/simulation.py](cycle06/simulation.py) | upcoming |
| 7 | B&H ch. 7 | Joint distributions | [cycle07/simulation.py](cycle07/simulation.py) | upcoming |
| 8 | B&H ch. 7 (cont.) | Joint distributions, continued | [cycle08/simulation.py](cycle08/simulation.py) | upcoming |
| 9 | Review | Midyear review of chapters 1–7 | [cycle09/simulation.py](cycle09/simulation.py) | upcoming |
| 10 | B&H ch. 9 | Conditional expectation | [cycle10/simulation.py](cycle10/simulation.py) | upcoming |
| 11 | B&H ch. 10 | Inequalities and limit theorems | [cycle11/simulation.py](cycle11/simulation.py) | upcoming |
| 12 | B&H ch. 11 | Markov chains | [cycle12/simulation.py](cycle12/simulation.py) | upcoming |
| 13 | OpenIntro ch. 5 | Foundations for inference | [cycle13/simulation.py](cycle13/simulation.py) | upcoming |
| 14 | OpenIntro ch. 6 | Inference for categorical data | [cycle14/simulation.py](cycle14/simulation.py) | upcoming |
| 15 | Regression | Linear regression | [cycle15/simulation.py](cycle15/simulation.py) | upcoming |
| 16 | Regression | Logistic regression | [cycle16/simulation.py](cycle16/simulation.py) | upcoming |
| 17 | Final project | Final project, part 1 | [cycle17/simulation.py](cycle17/simulation.py) | upcoming |
| 18 | Final project | Final project, part 2 | [cycle18/simulation.py](cycle18/simulation.py) | upcoming |

Each `cycleNN/` folder holds `problems.md` (the problem set), `log.md` (the half-page log) and
`simulation.py` (the program). `common/sim.py` is the small helper every program starts from.

## Running a program

Every program is a plain Python 3 script. From the repo root:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python cycle01/simulation.py
```

The early programs only need the standard library, so the virtual environment is optional until
a later cycle imports numpy, pandas or scikit-learn. Programs that take arguments say so in
their docstring; for example `python cycle01/simulation.py 30 20000` runs the birthday problem
for 30 people with 20,000 trials. Every program uses a fixed random seed, so running it twice
prints the same numbers.
