"""Small simulation helpers shared by every cycle's program.

Typical use:

    from common.sim import estimate, report

    def trial(rng):              # one run of the experiment
        return rng.random() < 0.5
    p = estimate(trial, n_trials=100_000)
    report("P(coin is heads)", simulated=p, exact=0.5)
"""
import random


def estimate(trial, n_trials=100_000, seed=0):
    """Run `trial(rng)` n_trials times; return the fraction that returned True.

    trial     a function that takes a random.Random object, runs the
              experiment once, and returns True if the event happened.
    n_trials  how many times to run it. More trials means less noise
              (the error shrinks like 1/sqrt(n_trials)) but takes longer.
    seed      fixed seed so the same program prints the same numbers every
              run. Pass seed=None to get fresh randomness each time.
    """
    rng = random.Random(seed)   # our own generator, so nothing else can disturb it
    successes = 0
    for _ in range(n_trials):
        if trial(rng):
            successes += 1
    return successes / n_trials


def report(label, simulated, exact):
    """Print the simulated value next to the exact one, and the gap between them."""
    print(label)
    print(f"  simulated = {simulated:.4f}")
    print(f"  exact     = {exact:.4f}")
    print(f"  gap       = {simulated - exact:+.4f}")
