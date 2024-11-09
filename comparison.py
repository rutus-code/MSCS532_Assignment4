import random
import time
from copy import deepcopy
import matplotlib.pyplot as plt
from heapSort import heapsort  # Import heapSort function directly

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Function to measure execution time of sorting functions
def measure_time(sort_func, arr):
    start_time = time.time()
    sort_func(arr)
    end_time = time.time()
    return end_time - start_time

# Arrays for testing
sizes = [100, 1000, 5000, 10000]
types = ['random', 'sorted', 'reverse']

# Data collection
results = {t: {"sizes": sizes, "heapsort": [], "quicksort": [], "mergesort": []} for t in types}

# Perform tests
for size in sizes:
    for t in types:
        if t == 'random':
            arr = [random.randint(0, size) for _ in range(size)]
        elif t == 'sorted':
            arr = list(range(size))
        elif t == 'reverse':
            arr = list(range(size, 0, -1))
        
        # Measure and store execution times
        results[t]["heapsort"].append(measure_time(heapsort, deepcopy(arr)))
        results[t]["quicksort"].append(measure_time(quicksort, deepcopy(arr)))
        results[t]["mergesort"].append(measure_time(mergesort, deepcopy(arr)))

# Plotting the results
for t in types:
    plt.figure(figsize=(10, 6))
    plt.plot(results[t]["sizes"], results[t]["heapsort"], label="Heapsort", marker='o')
    plt.plot(results[t]["sizes"], results[t]["quicksort"], label="Quicksort", marker='o')
    plt.plot(results[t]["sizes"], results[t]["mergesort"], label="Mergesort", marker='o')
    
    plt.xlabel("Array Size")
    plt.ylabel("Time (seconds)")
    plt.title(f"Sorting Performance Comparison - {t.capitalize()} Array")
    plt.legend()
    plt.grid(True)
    plt.show()
