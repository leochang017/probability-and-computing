""" simulation helpers shared by every cycle's program.

"""
import random


def estimate(trial, n_trials=100_000, seed=0):
    """Run `trial(rng)` n_trials times; return the fraction that returned True.

    trial     a function that takes a random.Random object, runs the
              experiment once, and returns True if the event happened.
    n_trials  how many times to run it. 
    seed      fixed seed so the same program prints the same numbers every
              run. 
    """
    rng = random.Random(seed)  # creates random generator
    successes = 0
    for _ in range(n_trials):
        if trial(rng):
            successes += 1
    return successes / n_trials


def report(label, simulated, exact):
    """Print the simulated value next to the exact one, and the gap between them."""
    print(label)
    print(f"  simulated = {simulated:.4f}") # 4 decimal places
    print(f"  exact     = {exact:.4f}")
    print(f"  gap       = {simulated - exact:+.4f}")
