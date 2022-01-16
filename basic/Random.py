import random

arr = ["Hi", "Who", "What"]


# Random float number
print(random.random())

#random min-max
print(random.randint(0, 100))

#random by bit 2^n
print(random.getrandbits(2))

# random min - max - step
print(random.randrange(0, 100, 3))

# random specified list
print(random.choice(arr))

#random specified list with weight ratio
print(random.choices(arr, weights = (2,4,2), k = 9))

#random suffle specified list
random.shuffle(arr)
print(arr)

#random list with specified list
print(random.sample(arr, k = 2))

#random float number min-max
print(random.uniform(20, 60))

#random float number with min-max and mode
print(random.triangular(0, 10, 5))