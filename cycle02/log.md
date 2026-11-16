# Cycle 2 — Log

**Chapter:** B&H ch. 2 — Conditional probability  
**Date:** 2026-11-12

## What I learned
Conditional probability is the way a probability changes when you learn something else has occurred. The major techniques I used to do this were the definition of P(A | B) = P(A and B)/P(B), Bayes' Rule to flip P(B | A) into P(A | B), and the Law of Total Probability to break a problem down into parts. I also defined independent events and showed how two things could be independent based upon a third thing, even though they were not independent on their own. I also examined the Monty Hall Problem and Simpson's Paradox in lecture six.

Most surprising about conditional probability was how important my initial probability was. In the case of the two spam filters, a filter that was 90% accurate and said an email was good would have only a .5 probability of being correct as there weren't many legitimate emails.

## What was hard
It was difficult to keep P(A|B) and P(B|A) distinct from one another. Although they both appear to represent the same idea, these values will typically be significantly different. The two children problem was my most difficult problem in this chapter because of the fact that "at least one child is a boy" and "the child I see is a boy", although sounding almost alike, produced 1/3 and 1/2 respectively.

As far as the program, the greatest difficulty was determining why the filter uses the log function versus multiplication of the word probabilities, as well as the reason each word count receives a +1.

## What I'm changing
For conditional probability problems I'm going to write down what each event is and exactly what I'm given before using any formula because the easiest mistake in this chapter is mixing up which thing is the condition.