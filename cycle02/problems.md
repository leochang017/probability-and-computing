# Cycle 2 — Problem Set

**Cycle:** 2  
**Chapter:** B&H ch. 2 — Conditional probability  

Problems 1–6 are textbook exercises. Problems 7–8 are finance interview problems.

---

## Problem 1

**Source:** B&H Exercise 2.1

**Problem:**

A spam filter is designed by looking at commonly occurring phrases in spam. Suppose that 80% of email is spam. In 10% of the spam emails, the phrase "free money" is used, whereas this phrase is only used in 1% of non-spam emails. A new email has just arrived, which does mention "free money". What is the probability that it is spam?

**Solution:**

Let S = the email is spam, F = it contains "free money". I know P(S) = 0.8, P(F | S) = 0.1 and P(F | not S) = 0.01, and I want P(S | F).

Bayes' rule, with the law of total probability for the bottom:

P(S | F) = P(F | S) P(S) / [P(F | S) P(S) + P(F | not S) P(not S)]

= (0.1 · 0.8) / (0.1 · 0.8 + 0.01 · 0.2) = 0.08 / 0.082 = 80/82 ≈ **0.9756**

Another way to see it: out of 1000 emails, 800 are spam and 80 of those say "free money". 200 are not spam and 2 of those say it. So 80 of the 82 "free money" emails are spam. This is the same calculation my cycle 2 program does for the word "free".

---

## Problem 2

**Source:** B&H Exercise 2.2

**Problem:**

A woman is pregnant with twin boys. Twins may be either identical or fraternal (non-identical). In general, 1/3 of twins born are identical. Obviously, identical twins must be of the same sex; fraternal twins may or may not be. Assume that identical twins are equally likely to be both boys or both girls, while for fraternal twins all possibilities are equally likely. Given the above information, what is the probability that the woman's twins are identical?

**Solution:**

Let I = identical, BB = both boys. P(I) = 1/3.

- P(BB | I) = 1/2, because identical twins are either both boys or both girls.
- P(BB | fraternal) = 1/4, because the four possibilities BB, BG, GB, GG are equally likely.

P(I | BB) = P(BB | I) P(I) / [P(BB | I) P(I) + P(BB | fraternal) P(fraternal)]

= (1/2 · 1/3) / (1/2 · 1/3 + 1/4 · 2/3) = (1/6) / (1/6 + 1/6) = **1/2**

Knowing they're both boys moves the probability up from 1/3 to 1/2, because "same sex" is more likely for identical twins than for fraternal ones.

---

## Problem 3

**Source:** B&H Exercise 2.22

**Problem:**

A bag contains one marble which is either green or blue, with equal probabilities. A green marble is put in the bag (so there are 2 marbles now), and then a random marble is taken out. The marble taken out is green. What is the probability that the remaining marble is also green?

**Solution:**

Let A = the original marble was green, B = the marble taken out is green. The remaining marble is green exactly when the original marble was green (then both are green, and whichever one I take leaves a green one). So I need P(A | B).

- P(B | A) = 1, both marbles are green.
- P(B | not A) = 1/2, one green and one blue.

P(A | B) = (1 · 1/2) / (1 · 1/2 + 1/2 · 1/2) = (1/2) / (3/4) = **2/3**

It's tempting to say 1/2, since the original marble was 50/50. But pulling out a green marble is evidence: it happens every time when the bag is green-green and only half the time when it's green-blue.

---

## Problem 4

**Source:** B&H Exercise 2.26

**Problem:**

To battle against spam, Bob installs two anti-spam programs. An email arrives, which is either legitimate (event L) or spam (event L^c), and which program j marks as legitimate (event M_j) or marks as spam (event M_j^c) for j in {1, 2}. Assume that 10% of Bob's email is legitimate and that the two programs are each "90% accurate" in the sense that P(M_j | L) = P(M_j^c | L^c) = 9/10. Also assume that given whether an email is spam, the two programs' outputs are conditionally independent.

(a) Find the probability that the email is legitimate, given that the 1st program marks it as legitimate.

(b) Find the probability that the email is legitimate, given that both programs mark it as legitimate.

(c) Bob runs the 1st program and M_1 occurs. He updates his probabilities and then runs the 2nd program. Is conditioning on M_1 and M_2 in one step equivalent to first conditioning on M_1, updating, and then conditioning on M_2?

**Solution:**

P(L) = 1/10. P(M_j | L) = 9/10. A spam email gets marked legitimate with probability P(M_j | L^c) = 1/10.

(a) P(L | M_1) = (9/10 · 1/10) / (9/10 · 1/10 + 1/10 · 9/10) = (9/100) / (18/100) = **1/2**

A "90% accurate" program saying an email is fine only makes it 50/50, because legitimate email is so rare to begin with.

(b) Conditional independence lets me multiply the two programs' probabilities once I know whether the email is spam:

P(M_1, M_2 | L) = (9/10)^2 = 81/100 and P(M_1, M_2 | L^c) = (1/10)^2 = 1/100

P(L | M_1, M_2) = (81/100 · 1/10) / (81/100 · 1/10 + 1/100 · 9/10) = 81 / (81 + 9) = **9/10**

(c) Yes, it's the same. After the first program my probability of L is 1/2 from part (a). Using that as the new prior and updating on M_2:

(9/10 · 1/2) / (9/10 · 1/2 + 1/10 · 1/2) = 9/10

which matches (b). The order I take in the evidence doesn't change where I end up.

---

## Problem 5

**Source:** B&H Exercise 2.30

**Problem:**

A family has 3 children, creatively named A, B, and C.

(a) Discuss intuitively (but clearly) whether the event "A is older than B" is independent of the event "A is older than C".

(b) Find the probability that A is older than B, given that A is older than C.

**Solution:**

(a) They are not independent. If I learn A is older than C, that tells me A is more likely to be near the top of the birth order, so it's more likely A is also older than B. It's easier to see with more kids: if A is older than 50 siblings, I'd bet A is older than the next one too.

(b) There are 3! = 6 equally likely birth orders (oldest first):

ABC, ACB, BAC, BCA, CAB, CBA

A is older than C in three of them: ABC, ACB, BAC. Out of those three, A is also older than B in ABC and ACB.

P(A older than B | A older than C) = **2/3**

Same thing with the definition: P(A older than both) = P(A is the eldest) = 1/3, and P(A older than C) = 1/2, so (1/3)/(1/2) = 2/3. Since 2/3 is not 1/2, this confirms they're dependent.

---

## Problem 6

**Source:** B&H Exercise 2.38

**Problem:**

(a) Consider the following 7-door version of the Monty Hall problem. There are 7 doors, behind one of which there is a car (which you want), and behind the rest of which there are goats (which you don't want). Initially, all possibilities are equally likely for where the car is. You choose a door. Monty Hall then opens 3 goat doors, and offers you the option of switching to any of the remaining 3 doors. Assume that Monty Hall knows which door has the car, will always open 3 goat doors and offer the option of switching, and that Monty chooses with equal probabilities from all his choices of which goat doors to open. Should you switch? What is your probability of success if you switch to one of the remaining 3 doors?

(b) Generalize the above to a Monty Hall problem where there are n ≥ 3 doors, of which Monty opens m goat doors, with 1 ≤ m ≤ n − 2.

**Solution:**

(a) If I stay, I win only if my first pick was right, which is 1/7. Monty opening goat doors doesn't change that, because he can always open 3 goat doors no matter what I picked, so him doing it tells me nothing about my own door.

That leaves 6/7 for the car being behind one of the other 6 doors. Monty showed that 3 of those are goats, so the whole 6/7 sits on the 3 closed doors I didn't pick. By symmetry they share it equally: (6/7)/3 = 2/7 each.

So I should switch. Switching wins with probability **2/7**, compared to 1/7 for staying.

(b) Same argument. Staying wins with probability 1/n. The other (n − 1)/n is spread equally over the n − m − 1 doors that are still closed and aren't mine.

P(win by switching) = **(n − 1) / (n (n − m − 1))**

This is bigger than 1/n because (n − 1)/(n − m − 1) > 1 whenever m ≥ 1, so switching is always better. Check with the original problem, n = 3 and m = 1: (2)/(3 · 1) = 2/3.

---

## Problem 7

**Source:** Zhou ch. 4 (Boys and girls)

**Problem:**

Part A. A company holds a dinner for working mothers who have at least one son. Ms. Jackson, a mother with two children, is invited. What is the probability that both of her children are boys?

Part B. Your new colleague, Ms. Parker, is known to have two children. You see her walking with one of her children, and that child is a boy. What is the probability that both of her children are boys?

**Solution:**

For two children there are four equally likely cases, written older child first: BB, BG, GB, GG.

Part A. "At least one son" rules out only GG. That leaves BB, BG, GB, still equally likely, and one of them is two boys.

P(BB | at least one boy) = (1/4) / (3/4) = **1/3**

Part B. This is different information. I saw one particular child, and that child is a boy. The other child is just a separate kid who is a boy or a girl with probability 1/2 each, so the answer is **1/2**.

With Bayes' rule: let S = the child I happened to see is a boy. P(S | BB) = 1, P(S | BG) = P(S | GB) = 1/2, P(S | GG) = 0.

P(BB | S) = (1 · 1/4) / (1 · 1/4 + 1/2 · 1/4 + 1/2 · 1/4 + 0) = (1/4) / (1/2) = 1/2

The two parts sound the same but they aren't. In part A a two-boy family and a one-boy family both get invited for sure. In part B a two-boy family is twice as likely to show me a boy as a one-boy family is, and that extra weight on BB moves the answer from 1/3 to 1/2.

---

## Problem 8

**Source:** Zhou ch. 4 (Unfair coin)

**Problem:**

You are given 1000 coins. One of them has heads on both sides and the other 999 are fair. You pick a coin at random and toss it 10 times, and it comes up heads all 10 times. What is the probability that the coin you picked is the unfair one?

**Solution:**

Let U = I picked the two-headed coin, H = 10 heads in a row.

- P(U) = 1/1000 and P(H | U) = 1.
- P(not U) = 999/1000 and P(H | not U) = (1/2)^10 = 1/1024.

P(U | H) = (1 · 1/1000) / (1 · 1/1000 + 1/1024 · 999/1000)

Multiply top and bottom by 1000 · 1024:

= 1024 / (1024 + 999) = 1024/2023 ≈ **0.506**

So it's basically a coin flip whether I'm holding the unfair coin. Ten heads in a row is about a 1-in-1000 event for a fair coin, and picking the unfair coin was also a 1-in-1000 event, so the two explanations end up about equally likely.
