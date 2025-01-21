import random
import sys
sys.setrecursionlimit(200000)  # Increase recursion limit to 2000

# Use Randomized Pivot Selection
# To avoid repeatedly selecting the worst-case pivot, choose a random pivot index. 
# This reduces the likelihood of unbalanced partitions.

# Function to find the partition position
def partition(array, low, high):
    """
    Partitions the array into two halves around a pivot element.
    Randomly selects a pivot to reduce the chance of worst-case performance.
    """
    pivot_index = random.randint(low, high)
    array[pivot_index], array[high] = array[high], array[pivot_index]
    
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            # Swap elements to place smaller element on the correct side
            i += 1
            array[i], array[j] = array[j], array[i]

    # Place the pivot element at the correct position
    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

# Quick Sort function
def quickSort(array, low, high):
    """
    Performs Quick Sort on the input array in place.
    """
    if low < high:
        # Partition the array
        pi = partition(array, low, high)

        # Sort the elements on the left of the pivot
        quickSort(array, low, pi - 1)

        # Sort the elements on the right of the pivot
        quickSort(array, pi + 1, high)


# Quick Sort that returns a new sorted array
def quick_sort(array):
    """
    Wrapper for Quick Sort that sorts the array and returns a new sorted list.
    """
    array_copy = array.copy()  # To avoid modifying the original array
    quickSort(array_copy, 0, len(array_copy) - 1)

    return array_copy



