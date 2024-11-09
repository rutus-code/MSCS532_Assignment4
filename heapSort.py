#Created By : Rutu Shah
# Created Date :  9th November 2024
#implementation of Heap Sort

def heapify(arr, n, i):
    #initialize root node as largest
    largest = i  
    #left child node initialization
    left = 2 * i + 1  
    #right child node initialization
    right = 2 * i + 2  

    # if left child node exists and is greater than root, then swap
    if left < n and arr[left] > arr[largest]:
        largest = left

    # if right child node exists and is greater than the current largest, then swap
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and continue heapifying
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        arr[i], arr[0] = arr[0], arr[i]  
        # Call heapify on the reduced heap
        heapify(arr, i, 0)  

# Example usage
arr = [25, 45, 1, 66, 5,14,19,9]
heapsort(arr)
print("Sorted array is:", arr)
