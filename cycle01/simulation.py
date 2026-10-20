import sys 
from pathlib import Path 
sys.path.insert(0, str(Path(__file__).resolve().parent.parent)) 
from common.sim import estimate, report

DAYS = 365

def has_shared_birthday (rng, people):
    birthdays = []
    for i in range(people):
        birthdays.append(rng.randint(1, DAYS)) # making random birthdays by adding one random number to the end "people" times
    return len(set(birthdays)) < people # checking if there is a repeat birthday b/c set(birthdays) can't have duplicates, so if it's less than the count of people, there has to be a duplicate; returns True or False

def exact_match_probability (people):
    p_no_match = 1.0 # counter for the probability of no match
    for i in range(people):
        p_no_match = p_no_match * (DAYS - i) / DAYS # for each person, the probability of not matching is (DAYS - i) / DAYS, where i is the number of people already accounted for; multiply these probabilities together to get the overall probability of no match
    return 1 - p_no_match # the probability of at least one match is 1 minus the probability of no match
    
def main():
    """for people in [23, 50, 70]:
        simulated = estimate(lambda rng: has_shared_birthday(rng, people), 100_000) # runs the simulation 100,000 times for each number of people and estimates the probability of a shared birthday
        exact = exact_match_probability(people) # calculates the exact probability of a shared birthday for the given number of people
        report(f"P(shared birthday) with {people} people", simulated, exact) # reports the results of the simulation and the exact calculation
        print()"""
    
    group_sizes = [23, 50, 70]
    n_trials = 100_000 # these are default values if the user doesn't type anything

    if len(sys.argv) > 1: 
        group_sizes = [int(sys.argv[1])] #if there is at least one argiment after the script name, replace the default list with a one-item list containing that number
    if len(sys.argv) > 2:
        n_trials = int(sys.argv[2]) # if there is a second argument, use it as the number of trials
    for people in group_sizes:
        simulated = estimate(lambda rng: has_shared_birthday(rng, people), n_trials)
        exact = exact_match_probability(people)
        report(f"P(shared birthday) with {people} people", simulated, exact)
        print()

if __name__ == "__main__":
    main()