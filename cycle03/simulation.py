import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from common.sim import estimate, report


def reaches_goal(rng, start, goal, p):
    # money is how many dollars I have right now, it starts at whatever I walked in with
    money = start
    # keep betting as long as I'm not broke (0) and haven't hit the goal yet
    while 0 < money < goal:
        # rng.random() gives a random decimal between 0 and 1, so it's below p exactly p of the time
        if rng.random() < p:
            # won the bet, up a dollar
            money += 1
        else:
            # lost the bet, down a dollar
            money -= 1
    # the loop only ends at 0 or at the goal, so this is True if I made it and False if I went broke
    return money == goal


def exact_win_probability(start, goal, p):
    # q is the chance of losing one bet
    q = 1 - p
    # fair game is its own case because the other formula would divide by zero
    if p == q:
        # with a fair coin the answer is just how far along I already am, like 10 out of 20 = 0.5
        return start / goal
    # ratio is q/p, it's bigger than 1 when the game is against me
    ratio = q / p
    # textbook formula for the unfair game: (1 - (q/p)^start) / (1 - (q/p)^goal)
    return (1 - ratio ** start) / (1 - ratio ** goal)


def main():
    # default setup: walk in with $10 and try to double it to $20
    start = 10
    goal = 20
    n_trials = 100_000

    # optional arguments typed after the file name: start, goal, number of trials
    if len(sys.argv) > 1:
        start = int(sys.argv[1])
    if len(sys.argv) > 2:
        goal = int(sys.argv[2])
    if len(sys.argv) > 3:
        n_trials = int(sys.argv[3])

    # three games to compare: a fair coin, a coin that's slightly against me, and betting on red in roulette
    # (18 red slots out of 38 on an American wheel)
    games = [
        ("fair coin, p = 0.5", 0.5),
        ("slightly unfair, p = 0.49", 0.49),
        ("roulette on red, p = 18/38", 18 / 38),
    ]

    for name, p in games:
        simulated = estimate(lambda rng, p=p: reaches_goal(rng, start, goal, p), n_trials)
        # the answer from the formula, to compare against
        exact = exact_win_probability(start, goal, p)
        report(f"P(reach ${goal} before $0, starting with ${start}) | {name}", simulated, exact)
        print()


if __name__ == "__main__":
    main()


"""python3 cycle03/simulation.py
  python3 cycle03/simulation.py 5 20
  python3 cycle03/simulation.py 50 100 20000

  - With no arguments it starts at $10, aims for $20, and plays 100,000 games per coin.
  - The arguments are starting money, goal, and number of games, in that order.
"""