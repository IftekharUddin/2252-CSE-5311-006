import timeit
import random
import psutil
import platform
import matplotlib.pyplot as plt

from BubbleSort import bubble_sort
from InsertionSort import insertion_sort
from SelectionSort import  selection_sort
from MergeSort import merge_sort

# Function to Benchmark Sorting Algorithms
def benchmark_sorting(algorithm, sizes):
    times = []
    for size in sizes:
        arr = [random.randint(0, 10000) for _ in range(size)]  # Generate random array
        timer = timeit.timeit(lambda: algorithm(arr.copy()), number=1)  # Measure runtime
        times.append(timer)
        print(f"{algorithm.__name__} | Size: {size} | Time: {timer:.6f} sec")
    return times

# Get System Info
def get_system_info():
    cpu_info = platform.processor()
    ram_info = round(psutil.virtual_memory().total / (1024**3), 2)  # Convert bytes to GB
    return f"CPU: {cpu_info}, RAM: {ram_info} GB"

# Define Input Sizes
sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

# Run Benchmarking
print("System Info:", get_system_info())

insertion_times = benchmark_sorting(insertion_sort, sizes)
selection_times = benchmark_sorting(selection_sort, sizes)
bubble_times = benchmark_sorting(bubble_sort, sizes)

# Plot Results
plt.figure(figsize=(10, 6))
plt.plot(sizes, insertion_times, marker='o', label="Insertion Sort")
plt.plot(sizes, selection_times, marker='s', label="Selection Sort")
plt.plot(sizes, bubble_times, marker='^', label="Bubble Sort")

plt.xlabel("Input Size (n)")
plt.ylabel("Time (seconds)")
plt.title("Sorting Algorithm Benchmarking")
plt.legend()
plt.grid(True)
plt.show()
