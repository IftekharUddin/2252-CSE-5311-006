import time
import random
import matplotlib.pyplot as plt
import numpy as np

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Non-random pivot 
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def quicksort_random(arr):
    if len(arr) <= 1:
        return arr
    pivot = random.choice(arr)  # Random pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort_random(left) + middle + quicksort_random(right)

def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    return time.time() - start_time

sizes = [100, 500, 1000, 5000, 10000]

best_case_times = []
worst_case_times = []
average_case_times = []

for n in sizes:
    best_case = list(range(n))  # Already sorted input
    worst_case = list(range(n, 0, -1))  # Reverse sorted input
    average_case = [random.randint(0, n) for _ in range(n)]  # Random input

    best_case_times.append(measure_time(quicksort, best_case))
    worst_case_times.append(measure_time(quicksort, worst_case))
    average_case_times.append(measure_time(quicksort, average_case))

# Plot results
plt.figure()
plt.plot(sizes, best_case_times, label='Best Case (Sorted Input)', marker='o')
plt.plot(sizes, worst_case_times, label='Worst Case (Reverse Sorted)', marker='o')
plt.plot(sizes, average_case_times, label='Average Case (Random Input)', marker='o')
plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Quicksort Performance (Non-Random Pivot)")
plt.legend()
plt.grid()
plt.show()