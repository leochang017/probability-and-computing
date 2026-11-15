# Cycle 3 — Problem Set

**Cycle:** 3  
**Chapter:** B&H ch. 3 — Random variables and their distributions  

Problems 1–6 are textbook exercises. Problems 7–8 are finance interview problems.

Notation: C(n, k) means "n choose k". Bin(n, p) is the Binomial distribution, the number of successes in n independent tries that each succeed with probability p.

---

## Problem 1

**Source:** B&H Exercise 3.6

**Problem:**

Benford's law states that in a very large variety of real-life data sets, the first digit approximately follows a particular distribution with about a 30% chance of a 1, an 18% chance of a 2, and in general

P(D = j) = log10((j + 1)/j), for j in {1, 2, 3, ..., 9},

where D is the first digit of a randomly chosen element. Check that this is a valid PMF (using properties of logs, not with a calculator).

**Solution:**

A PMF needs two things: every value is at least 0, and the values add up to 1.

Nonnegative: (j + 1)/j is bigger than 1 for every j from 1 to 9, and the log of a number bigger than 1 is positive.

Adds to 1: use log(a/b) = log(a) − log(b) to split each term.

Sum from j = 1 to 9 of [log10(j + 1) − log10(j)]

= (log 2 − log 1) + (log 3 − log 2) + (log 4 − log 3) + ... + (log 10 − log 9)

Every term in the middle cancels with its neighbor, and what's left is log10(10) − log10(1) = 1 − 0 = **1**.

Both conditions hold, so it's a valid PMF.

---

## Problem 2

**Source:** B&H Exercise 3.18

**Problem:**

(a) In the World Series of baseball, two teams (call them A and B) play a sequence of games against each other, and the first team to win four games wins the series. Let p be the probability that A wins an individual game, and assume that the games are independent. What is the probability that team A wins the series?

(b) Give a clear intuitive explanation of whether the answer to (a) depends on whether the teams always play 7 games (and whoever wins the majority wins the series), or the teams stop playing more games as soon as one team has won 4 games.

**Solution:**

Let q = 1 − p.

(a) Pretend they always play all 7 games (part (b) explains why that's allowed). Let X be the number of games A wins. Then X is Bin(7, p), and A wins the series exactly when X ≥ 4.

P(A wins the series) = C(7, 4) p^4 q^3 + C(7, 5) p^5 q^2 + C(7, 6) p^6 q + p^7

= **35 p^4 q^3 + 21 p^5 q^2 + 7 p^6 q + p^7**

Check: at p = 1/2 this is (35 + 21 + 7 + 1)/128 = 64/128 = 1/2, which is what it should be for evenly matched teams.

The direct way gives the same thing. For A to win in exactly k games, A wins game k and exactly 3 of the k − 1 games before it:

p^4 + C(4, 3) p^4 q + C(5, 3) p^4 q^2 + C(6, 3) p^4 q^3

(b) It doesn't depend on it. Once a team has 4 wins, the other team can have at most 3 even if all 7 games are played, so any extra games can't change who won. Stopping early and "first to 4 out of 7" always produce the same winner, so they have the same probability.

---

## Problem 3

**Source:** B&H Exercise 3.25

**Problem:**

Alice flips a fair coin n times and Bob flips another fair coin n + 1 times, resulting in independent X ~ Bin(n, 1/2) and Y ~ Bin(n + 1, 1/2).

(a) Show that P(X < Y) = P(n − X < n + 1 − Y).

(b) Compute P(X < Y).

**Solution:**

(a) X counts Alice's heads, so n − X counts her tails. Because the coin is fair, tails behave exactly like heads, so n − X is also Bin(n, 1/2). Same for Bob: n + 1 − Y is his number of tails and is Bin(n + 1, 1/2). They're still independent.

So the pair (n − X, n + 1 − Y) has the same distribution as the pair (X, Y), and any probability about one pair equals the same probability about the other. That gives P(X < Y) = P(n − X < n + 1 − Y). In words, "Bob gets more heads than Alice" is as likely as "Bob gets more tails than Alice".

(b) Simplify the right side. n − X < n + 1 − Y is the same as Y < X + 1. Since X and Y are whole numbers, Y < X + 1 is the same as Y ≤ X.

So P(X < Y) = P(Y ≤ X). But "Y ≤ X" is the complement of "X < Y", so

P(X < Y) = 1 − P(X < Y), which means P(X < Y) = **1/2**

Bob has an extra flip, and that extra flip is exactly enough to make it 50/50 that he ends up with strictly more heads, for any n.

---

## Problem 4

**Source:** B&H Exercise 3.28

**Problem:**

There are n eggs, each of which hatches a chick with probability p (independently). Each of these chicks survives with probability r, independently. What is the distribution of the number of chicks that hatch? What is the distribution of the number of chicks that survive? (Give the PMFs; also give the names of the distributions and their parameters, if applicable.)

**Solution:**

Let H be the number that hatch. Each egg is its own independent try that succeeds with probability p, which is the Binomial story.

**H ~ Bin(n, p)**, with P(H = k) = C(n, k) p^k (1 − p)^(n − k) for k = 0, 1, ..., n.

Let X be the number that survive. Look at one egg from the start: it ends up as a surviving chick only if it hatches and then survives, which has probability p · r. The eggs are still independent, so it's the same story with a smaller success probability.

**X ~ Bin(n, pr)**, with P(X = k) = C(n, k) (pr)^k (1 − pr)^(n − k) for k = 0, 1, ..., n.

I don't need to work out the two stages separately. Redefining "success" as "hatches and survives" does it in one step.

---

## Problem 5

**Source:** B&H Exercise 3.35

**Problem:**

Players A and B take turns in answering trivia questions, starting with player A answering the first question. Each time A answers a question, she has probability p1 of getting it right. Each time B plays, he has probability p2 of getting it right.

(a) If A answers m questions, what is the PMF of the number of questions she gets right?

(b) If A answers m times and B answers n times, what is the PMF of the total number of questions they get right (you can leave your answer as a sum)? Describe exactly when/whether this is a Binomial distribution.

(c) Suppose that the first player to answer correctly wins the game (with no predetermined maximum number of questions that can be asked). Find the probability that A wins the game.

**Solution:**

(a) It's m independent tries with success probability p1, so it's Bin(m, p1):

P(k right) = C(m, k) p1^k (1 − p1)^(m − k), for k = 0, 1, ..., m.

(b) Let T be the total. To get T = k, A gets some number j right and B gets the other k − j. Add over every possible j:

P(T = k) = sum over j from 0 to k of [C(m, j) p1^j (1 − p1)^(m − j)] · [C(n, k − j) p2^(k − j) (1 − p2)^(n − k + j)]

for k = 0, 1, ..., m + n, where C(a, b) counts as 0 if b > a.

This is Binomial only when p1 = p2. Then all m + n questions are independent tries with the same success probability p, so T ~ Bin(m + n, p). If p1 ≠ p2 the tries don't all have the same probability, and that breaks the Binomial story.

(c) Let w = P(A wins). Look at the first round:

- A gets her question right (probability p1): A wins.
- A misses and B gets his right (probability (1 − p1) p2): B wins.
- Both miss (probability (1 − p1)(1 − p2)): the game is back where it started, so A wins with probability w again.

w = p1 + (1 − p1)(1 − p2) w

w [1 − (1 − p1)(1 − p2)] = p1

w = p1 / [1 − (1 − p1)(1 − p2)] = **p1 / (p1 + p2 − p1 p2)**

Check: if p1 = p2 = 1/2, w = (1/2)/(3/4) = 2/3. Going first is worth a lot.

---

## Problem 6

**Source:** B&H Exercise 3.42

**Problem:**

Let X be a random day of the week, coded so that Monday is 1, Tuesday is 2, etc. (so X takes values 1, 2, ..., 7, with equal probabilities). Let Y be the next day after X (again represented as an integer between 1 and 7). Do X and Y have the same distribution? What is P(X < Y)?

**Solution:**

Yes, they have the same distribution. If X is equally likely to be any day, then "the day after X" is also equally likely to be any day, so P(Y = j) = 1/7 for every j from 1 to 7. That's the same PMF as X.

But they're not the same random variable. Y = X + 1, except when X = 7 (Sunday), where Y wraps around to 1. So X < Y every time except when X = 7.

P(X < Y) = P(X ≠ 7) = **6/7**

Having the same distribution doesn't mean X and Y are equally likely to be the bigger one. That would be true if they were independent, but here Y is completely determined by X.

---

## Problem 7

**Source:** Zhou ch. 4 (Coin toss game)

**Problem:**

Two players, A and B, take turns tossing a fair coin, with A going first. The sequence of heads and tails is recorded. As soon as a head is followed immediately by a tail, the game ends, and the player who tossed that tail wins. What is the probability that A wins?

**Solution:**

Nothing can end the game until the first head shows up, so there are really two situations: "no head yet" and "the last toss was a head".

First, the "last toss was a head" situation. Let h be the probability that the player about to toss wins.

- They toss tails (1/2): that's HT, they win.
- They toss heads (1/2): now the other player is the one tossing after a head, so the other player wins with probability h, and the original player wins with probability 1 − h.

h = 1/2 + (1/2)(1 − h), which gives (3/2) h = 1, so h = 2/3.

Now the start of the game. Let a = P(A wins), where A tosses first with no head yet.

- A tosses tails (1/2): still no head, and now B is the one "going first" in a fresh game. B wins that with probability a, so A wins with probability 1 − a.
- A tosses heads (1/2): B is now tossing right after a head, so B wins with probability h = 2/3, and A wins with probability 1/3.

a = (1/2)(1 − a) + (1/2)(1/3)

(3/2) a = 1/2 + 1/6 = 2/3

a = **4/9**

Going first is a slight disadvantage here. A can't win on the very first toss, but B can win on the second.

---

## Problem 8

**Source:** Zhou ch. 4 (Cars on road)

**Problem:**

The probability of seeing at least one car on a highway during any 20-minute interval is 609/625. Assuming the chance of seeing a car is the same in every stretch of time and separate stretches are independent, what is the probability of seeing at least one car during any 5-minute interval?

**Solution:**

Split the 20 minutes into four 5-minute blocks. Let p be the probability of at least one car in a 5-minute block.

"At least one car in 20 minutes" is hard to work with directly, so use the complement. No car in 20 minutes means no car in all four blocks, and the blocks are independent:

P(no car in 20 minutes) = (1 − p)^4

I'm told this equals 1 − 609/625 = 16/625.

(1 − p)^4 = 16/625 = (2/5)^4

1 − p = 2/5

p = **3/5**

This is the same idea as the Binomial: four independent tries, and "at least one success" is 1 minus the probability of zero successes.
