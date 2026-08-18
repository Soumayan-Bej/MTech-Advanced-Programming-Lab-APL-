import time
import matplotlib.pyplot as plt

def linear(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i

def test_linear(a, x):
    t = time.perf_counter()
    for _ in range(100):
        linear(a, x)
    return (time.perf_counter() - t) / 100


n = range(1000, 10001, 1000)
linear_best, linear_avg, linear_worst = [], [], []

for size in n:
    a = list(range(size))

    linear_best.append(test_linear(a, a[0]))          
    linear_avg.append(test_linear(a, a[size // 2]))   
    linear_worst.append(test_linear(a, -1))           


def binary(a, x):
    l, r = 0, len(a) - 1
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            return m
        if a[m] < x:
            l = m + 1
        else:
            r = m - 1

def test_binary(a, x):
    t = time.perf_counter()
    for _ in range(100):
        binary(a, x)
    return (time.perf_counter() - t) / 100


binary_best, binary_avg, binary_worst = [], [], []

for size in n:
    a = list(range(size))

    binary_best.append(test_binary(a, a[size // 2]))  
    binary_avg.append(test_binary(a, a[size // 4]))   
    binary_worst.append(test_binary(a, -1))           


plt.figure()
plt.plot(n, linear_best, label="Best Case")
plt.plot(n, linear_avg, label="Average Case")
plt.plot(n, linear_worst, label="Worst Case")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Linear Search - Best, Average and Worst Case")
plt.legend()
plt.grid()
plt.show()


plt.figure()
plt.plot(n, binary_best, label="Best Case")
plt.plot(n, binary_avg, label="Average Case")
plt.plot(n, binary_worst, label="Worst Case")
plt.xlabel("Input Size (n)")
plt.ylabel("Execution Time (seconds)")
plt.title("Binary Search - Best, Average and Worst Case")
plt.legend()
plt.grid()
plt.show()