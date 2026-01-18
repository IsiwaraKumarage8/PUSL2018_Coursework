import random
import sys

def dice_simulation(trials):
    count_32 = 0

    for _ in range(trials):
        dice = [random.randint(1,6) for _ in range(10)]
        if sum(dice) == 32:
            count_32 += 1

    probability = count_32 / trials
    return count_32, probability

if __name__ == "__main__":
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 500
    count, prob = dice_simulation(trials)

    print("Number of trials:", trials)
    print("Number of times sum = 32:", count)
    print("Estimated probability:", prob)
