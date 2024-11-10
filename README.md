# MSCS532_Assignment4

## Created By: Rutu Shah
## Created Date : 9th November 2024

### Project Overview
This project consists of three Python scripts:

1. *heapSort.py:* Implements the heap sort algorithm, a comparison-based sorting technique that uses a binary heap data structure.

2. *comparisonOfHeapSort.py:* Compares the performance of heap sort with merge sort and quick sort algorithms across different types of arrays (random, sorted, and reverse sorted). It visualizes the time complexity using matplotlib.
3. **Task class**: Represents individual tasks with attributes such as `task_id`, `priority`, `arrival_time`, `deadline`, and any additional `data` using priority queue and max-heap to ensure the highest-priority task is served first

#### 1. heapSort.py
#### Description
The heapSort.py script contains a function to perform heap sort. It defines a helper function heapify to maintain the heap property, and a heapsort function that arranges the elements in ascending order by creating a max heap and extracting the largest element one-by-one.

#### How to Run
#### To run the heapSort.py script:
```
python heapSort.py
```
#### Example Usage
#### The script includes a sample array for testing purposes. The sorted result is printed to the console.
```
arr = [25, 45, 1, 66, 5, 14, 19, 9]
heapsort(arr)
print("Sorted array is:", arr)
```
### Expected output:
```
Sorted array is: [1, 5, 9, 14, 19, 25, 45, 66]
```
#### 2. comparisonOfHeapSort.py
#### Description
The comparisonOfHeapSort.py script compares the runtime performance of heap sort, quick sort, and merge sort across arrays of varying sizes (100, 1000, 5000, and 10000 elements) and types (random, sorted, and reverse sorted). The results are plotted using matplotlib to visualize the time complexity of each algorithm.

#### How to Run
#### To run the comparisonOfHeapSort.py script:
```
python comparisonOfHeapSort.py
```
Ensure that you have matplotlib installed:

```
pip install matplotlib
```

#### Example Usage
This script generates plots of sorting performance. Each plot displays the runtime of each algorithm on different array sizes and types.

#### Expected Output
The script will display three separate plots, each representing the performance comparison for a different array type (random, sorted, and reverse). The x-axis represents the array size, while the y-axis represents the time taken (in seconds) to sort the array.

#### Summary of Findings
#### *Heap Sort*: Shows stable performance across various input types but may be slower than quick sort for large random arrays.

#### *Quick Sort*: Typically the fastest for random arrays but has worse performance on already sorted or reverse sorted arrays due to its recursive nature.

#### *Merge Sort*: Performs consistently across all input types but is generally slower than quick sort on random arrays.

This comparison provides insight into the practical performance of sorting algorithms, demonstrating how array characteristics impact time complexity.

3. taskApplicationInPriorityQueue.py
### Features
- **Insert Task**: Adds a new task to the priority queue based on its priority.
- **Extract Max**: Retrieves and removes the highest-priority task.
- **Modify Priority**: Changes the priority of a specific task by its `task_id` and adjusts the heap structure.
- **Peek**: Views the highest-priority task without removing it.
- **Size and Is Empty**: Provides utility functions to check the queue size and whether it is empty.


### How to Run
1. Run the script to test the priority queue functionality:

   ```bash
    taskApplicationInPriorityQueue.py
