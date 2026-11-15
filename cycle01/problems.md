# Cycle 1 — Problem Set

**Cycle:** 1  
**Chapter:** B&H ch. 1 — Probability and counting  

Problems 1–6 are textbook exercises. Problems 7–8 are finance interview problems.

Notation: C(n, k) means "n choose k", the number of ways to pick k things out of n.

---

## Problem 1

**Source:** B&H Exercise 1.8

**Problem:**

(a) How many ways are there to split a dozen people into 3 teams, where one team has 2 people and the other two teams have 5 people each?

(b) How many ways are there to split a dozen people into 3 teams, where each team has 4 people?

**Solution:**

(a) Pick the 2-person team first: C(12, 2) = 66 ways. Then pick 5 of the remaining 10 for one of the teams of 5: C(10, 5) = 252 ways. The last 5 people are the other team.

That counts every split twice, because the two teams of 5 don't have names. Picking {A, B, C, D, E} "first" and leaving {F, G, H, I, J} is the same split as doing it the other way around. So divide by 2:

66 · 252 / 2 = **8316**

(b) If the teams had names (Team A, Team B, Team C), the count would be C(12, 4) · C(8, 4) · C(4, 4) = 495 · 70 · 1 = 34650. The teams don't have names, so every split got counted once for each way of ordering the 3 teams, which is 3! = 6 times.

34650 / 6 = **5775**

---

## Problem 2

**Source:** B&H Exercise 1.9

**Problem:**

(a) How many paths are there from the point (0, 0) to the point (110, 111) in the plane such that each step either consists of going one unit up or one unit to the right?

(b) How many paths are there from (0, 0) to (210, 211), where each step consists of going one unit up or one unit to the right, and the path has to go through (110, 111)?

**Solution:**

(a) Write a path as a string of R's and U's. To get to (110, 111) I need exactly 110 R's and 111 U's, so the string is 221 letters long. A path is decided once I choose which 110 of the 221 positions are R's.

Number of paths = **C(221, 110)**

(b) Split it into two legs. The first leg, (0, 0) to (110, 111), has C(221, 110) paths from part (a). The second leg, (110, 111) to (210, 211), needs 100 R's and 100 U's, so it has C(200, 100) paths. Any first leg can be paired with any second leg, so multiply:

Number of paths = **C(221, 110) · C(200, 100)**

---

## Problem 3

**Source:** B&H Exercise 1.22

**Problem:**

A certain family has 6 children, consisting of 3 boys and 3 girls. Assuming that all birth orders are equally likely, what is the probability that the 3 eldest children are the 3 girls?

**Solution:**

Only the positions of the girls in the birth order matter. There are C(6, 3) = 20 ways to choose which 3 of the 6 birth positions belong to girls, and all 20 are equally likely. Exactly one of them puts the girls in the first three positions.

P = 1/20 = **0.05**

Check by counting full orderings instead: there are 6! = 720 orders of the six children. The ones I want are any order of the 3 girls followed by any order of the 3 boys, which is 3! · 3! = 36. And 36/720 = 0.05, same answer.

---

## Problem 4

**Source:** B&H Exercise 1.23

**Problem:**

A city with 6 districts has 6 robberies in a particular week. Assume the robberies are located randomly, with all possibilities for which robbery occurred where equally likely. What is the probability that some district had more than 1 robbery?

**Solution:**

This is the birthday problem with 6 "days" and 6 "people", so I use the complement.

Each robbery can land in any of 6 districts, so there are 6^6 = 46656 equally likely outcomes. "No district had more than 1" means all 6 robberies were in different districts, which can happen in 6! = 720 ways.

P(some district had more than 1) = 1 − 720/46656 ≈ **0.9846**

It's almost certain, even though 6 robberies in 6 districts sounds like it should spread out evenly.

---

## Problem 5

**Source:** B&H Exercise 1.26

**Problem:**

A college has 10 (non-overlapping) time slots for its courses, and blithely assigns courses to time slots randomly and independently. A student randomly chooses 3 of the courses to enroll in. What is the probability that there is a conflict in the student's schedule?

**Solution:**

Complement again. No conflict means the 3 courses are in 3 different slots. The first course can be anywhere (10 out of 10), the second has to avoid the first one's slot (9 out of 10), and the third has to avoid both (8 out of 10).

P(no conflict) = (10 · 9 · 8) / 10^3 = 0.72

P(conflict) = 1 − 0.72 = **0.28**

---

## Problem 6

**Source:** B&H Exercise 1.48

**Problem:**

A card player is dealt a 13-card hand from a well-shuffled, standard deck of cards. What is the probability that the hand is void in at least one suit ("void in a suit" means having no cards of that suit)?

**Solution:**

"At least one" of several overlapping events means inclusion-exclusion. Let S, H, D, C be the events that the hand has no spades, hearts, diamonds, clubs.

- Void in one specific suit: all 13 cards come from the other 39, so the probability is C(39, 13) / C(52, 13). There are 4 suits to choose.
- Void in two specific suits: all 13 cards come from the other 26, so C(26, 13) / C(52, 13). There are C(4, 2) = 6 pairs of suits.
- Void in three specific suits: the hand is the entire fourth suit, which is 1 hand, so 1 / C(52, 13). There are 4 ways to choose the three suits.
- Void in all four: impossible, probability 0.

P(S ∪ H ∪ D ∪ C) = [4 · C(39, 13) − 6 · C(26, 13) + 4] / C(52, 13) ≈ **0.0511**

The first term alone is 0.0512, so almost all of it comes from being void in exactly one suit.

---

## Problem 7

**Source:** Zhou ch. 4 (Poker hands)

**Problem:**

A poker hand is 5 cards from a standard 52-card deck. What are the probabilities of getting four of a kind, a full house, and two pairs?

**Solution:**

There are C(52, 5) = 2,598,960 possible hands, all equally likely. For each type of hand I count how many there are.

Four of a kind: choose the rank that appears 4 times (13 ways), and all 4 suits are used. The fifth card is any of the other 48 cards.

13 · 48 = 624 hands, so P = 624 / 2,598,960 ≈ **0.00024**

Full house: choose the rank for the three of a kind (13 ways) and which 3 of its 4 suits (C(4, 3) = 4). Then choose a different rank for the pair (12 ways) and which 2 suits (C(4, 2) = 6).

13 · 4 · 12 · 6 = 3744 hands, so P = 3744 / 2,598,960 ≈ **0.00144**

Two pairs: choose the two ranks for the pairs together, C(13, 2) = 78, because the two pairs aren't ordered. Each pair has C(4, 2) = 6 choices of suits. The fifth card has to be a third rank, or else it becomes a full house, so 52 − 8 = 44 choices.

78 · 6 · 6 · 44 = 123,552 hands, so P = 123,552 / 2,598,960 ≈ **0.0475**

---

## Problem 8

**Source:** Zhou ch. 4 (Application letters)

**Problem:**

You are sending job applications to 5 firms. You have 5 addressed envelopes and 5 cover letters, one written for each firm. The letters get put into the envelopes completely at random, one per envelope. What is the probability that all 5 letters end up in the wrong envelope?

**Solution:**

It's easier to find the probability that at least one letter is in the right envelope and subtract from 1. Let E_i be the event that letter i is in its correct envelope.

- P(E_i) = 1/5, and there are 5 of these.
- P(E_i and E_j) = (1/5)(1/4) = 1/20, and there are C(5, 2) = 10 pairs.
- In general, k specific letters are all correct with probability (5 − k)!/5!, and there are C(5, k) ways to choose them, so the k-th term in inclusion-exclusion is C(5, k) · (5 − k)!/5! = 1/k!.

P(at least one correct) = 1 − 1/2! + 1/3! − 1/4! + 1/5! = 1 − 1/2 + 1/6 − 1/24 + 1/120 = 76/120

P(all wrong) = 1 − 76/120 = 44/120 = **11/30 ≈ 0.367**

So out of the 120 ways to stuff the envelopes, 44 get every single one wrong.
