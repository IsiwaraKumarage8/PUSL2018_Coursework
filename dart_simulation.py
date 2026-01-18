import random
import sys

def simulate_darts(n):
    hits = 0
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x*x + y*y <= 1:
            hits += 1

    probability = hits / n
    pi_estimate = 4 * probability
    return hits, probability, pi_estimate

if __name__ == "__main__":
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 1000
    hits, prob, pi = simulate_darts(n)

    print("Number of throws:", n)
    print("Hits inside circle:", hits)
    print("Hitting probability:", prob)
    print("Estimated value of π:", pi)
