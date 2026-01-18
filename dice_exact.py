from itertools import product

count = 0
total = 6**10

for outcome in product(range(1,7), repeat=10):
    if sum(outcome) == 32:
        count += 1

probability = count / total

print("Exact combinations:", count)
print("Exact probability:", probability)
