"""Cycle 1 — The birthday problem (Blitzstein & Hwang, section 1.4).

Blitzstein & Hwang show that in a group of 23 people the probability that at
least two share a birthday is 1 - (365 * 364 * ... * 343) / 365**23 = 0.5073, which
surprises most people because 23 is so much smaller than 365. This program checks
that number by brute force: it draws 23 random birthdays 100,000 times and counts
how often a repeat shows up. With the fixed seed it reports 0.5090 against the exact
0.5073 (gap +0.0017), and for 50 and 70 people it reports 0.9705 vs 0.9704 and 0.9991
vs 0.9992. The two columns agree because the simulated fraction is a sample mean of
100,000 independent 0/1 outcomes, and by the law of large numbers that mean settles
down to the true probability, with a standard error of only sqrt(0.5 * 0.5 / 100000)
= 0.0016, so the observed gap of 0.0017 is exactly the size of noise we should expect.

Usage:
    python cycle01/simulation.py                 # 23, 50 and 70 people, 100,000 trials
    python cycle01/simulation.py 30              # 30 people, 100,000 trials
    python cycle01/simulation.py 30 20000        # 30 people, 20,000 trials
"""
import sys
from pathlib import Path

# Let this file find common/sim.py no matter which folder you run it from.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from common.sim import estimate, report  # noqa: E402  (import after the path fix)

DAYS = 365   # ignore leap years


def has_shared_birthday(rng, people):
    """One trial: draw `people` random birthdays, return True if any two match."""
    birthdays = [rng.randint(1, DAYS) for _ in range(people)]
    # A set keeps only distinct values, so if the set is smaller than the
    # list, at least one birthday appeared twice.
    return len(set(birthdays)) < people


def exact_match_probability(people):
    """P(at least two of `people` share a birthday), computed exactly.

    P(no match) = (365/365) * (364/365) * ... * ((365 - people + 1)/365):
    the first person can have any birthday, the second must avoid 1 day,
    the third must avoid 2 days, and so on. We multiply the fractions one
    at a time instead of writing 365! / (365 - people)! because those
    factorials are astronomically large; the running product never is.
    """
    p_no_match = 1.0
    for i in range(people):
        p_no_match *= (DAYS - i) / DAYS
    return 1 - p_no_match


def main():
    group_sizes = [23, 50, 70]
    n_trials = 100_000

    # Optional command-line arguments: [people] [trials].
    if len(sys.argv) > 1:
        group_sizes = [int(sys.argv[1])]
    if len(sys.argv) > 2:
        n_trials = int(sys.argv[2])

    for people in group_sizes:
        # estimate() wants a function of rng alone, so wrap our trial
        # in a lambda that fills in the group size.
        simulated = estimate(lambda rng: has_shared_birthday(rng, people), n_trials)
        exact = exact_match_probability(people)
        report(f"P(shared birthday) with {people} people, {n_trials:,} trials",
               simulated, exact)
        print()


if __name__ == "__main__":
    main()
