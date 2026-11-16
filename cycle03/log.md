# Cycle 3 — Log

**Chapter:** B&H ch. 3 — Random variables and their distributions  
**Date:** 

## What I learned
A random variable is an amount whose size will depend upon what happens when a random experiment is performed; an example is the number of heads in ten coin flips. Each possible random variable has a distribution which describes how probable each potential value is. There are two ways to express a discrete random variable's distribution: using a Probability Mass Function (PMF), which lists the probability associated with each potential value, or a Cumulative Distribution Function (CDF), which lists the probability of having taken on one of the values or less than that value. This chapter defined four specific types of distributions called the Bernoulli, Binomial, Hypergeometric, and Discrete Uniform distributions. Of these, the Binomial distribution appeared in many problems. Most problems could be solved based on whether they fit into certain stories such as 'a series of n independent trials, with identical probabilities of success', rather than requiring additional counting to solve them.

Gambler's Ruin was discussed in Lecture 7. Gambler's Ruin is a situation in which someone starts with an initial sum of money, makes bets that cost $1, and stops once he reaches his goal or runs out of money. In my simulations I used the parameters of $10 to reach $20 as the target amounts. If we flip a fair coin then we will reach our target 50% of the time. If we flip a coin with a 49% chance of getting heads, then we will reach our target 40% of the time. Finally if we bet on red in Roulette, then we will reach our target only 26% of the time. My simulations matched the formulas in all of those cases. A disadvantage of a very small degree per bet can lead to a large disadvantage over a long period of play.

## What was hard
Understanding the relationship between a random variable and its distribution. For example, X and "the day after X" have the same distribution but X occurs before "the day after X" 6/7 of the time. 

## What I'm changing
From now on I plan to verify every single formula I create with a simple case such as when p = 1/2, since I always know what should come from it and thus can easily detect any errors in my algebra.