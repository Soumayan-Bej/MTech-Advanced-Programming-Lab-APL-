import random
import time
import matplotlib.pyplot as plt
from collections import defaultdict

N = 10_000
REPEAT = 10

linear = [defaultdict(list) for _ in range(3)]
binary = [defaultdict(list) for _ in range(3)]


def linear_search(a, x):
    for i, v in enumerate(a):
        if v == x:
            return i
    return -1


def binary_search(a, x):
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m
        if a[m] < x:
            l = m + 1
        else:
            r = m - 1
    return -1


def measure(func, a, x):
    t = time.perf_counter()
    for _ in range(REPEAT):
        func(a, x)
    return (time.perf_counter() - t) / REPEAT


for _ in range(N):
    n = random.randint(5, 1000)
    a = sorted(random.sample(range(1, 10_000_001), n))


    for i, x in enumerate([a[0], a[random.randrange(n)], 10_000_001]):
        linear[i][n].append(measure(linear_search, a, x))


    for i, x in enumerate([a[n // 2], a[random.randrange(n)], 10_000_001]):
        binary[i][n].append(measure(binary_search, a, x))


def plot(data, title):
    x = sorted(set().union(*data))
    labels = ["Best Case", "Average Case", "Worst Case"]

    for i in range(3):
        y = [sum(data[i][n]) / len(data[i][n]) for n in x]
        plt.plot(x, y, label=labels[i])

    plt.xlabel("Input Size (n)")
    plt.ylabel("Average Execution Time (seconds)")
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


plot(linear, "Linear Search - Experimental Time Complexity")
plot(binary, "Binary Search - Experimental Time Complexity")