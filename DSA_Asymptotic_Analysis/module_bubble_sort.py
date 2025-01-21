def bubble_sort(arr):
    """
    Sorts an array using the Bubble Sort algorithm.
    """
    n = len(arr)
    for i in range(n):
        # Flag to detect if any swaps are made in the current pass
        swapped = False
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if the element is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no swaps were made, the array is already sorted
        if not swapped:
            break
    return arr
