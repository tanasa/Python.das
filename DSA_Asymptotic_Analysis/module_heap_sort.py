
def heapify(arr, n, i):
    """
    Maintains the heap property for a subtree rooted at index i.
    arr: The array to heapify.
    n: Size of the heap.
    i: Root index of the subtree.
    """
    largest = i  # Assume the root is the largest
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap it with the largest child
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap values
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)


def heap_sort(arr):
    """
    Performs Heap Sort on the given array and returns the sorted array.
    arr: The array to sort.
    Returns:
        A sorted list.
    """
    arr = arr.copy()  # To avoid modifying the original array
    n = len(arr)

    # Step 1: Build a max heap from the input array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Step 2: Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        # Move the current root (largest) to the end of the array
        arr[i], arr[0] = arr[0], arr[i]
        # Restore the max-heap property for the reduced heap
        heapify(arr, i, 0)
    
    # Step 3: Return the sorted array
    return arr


