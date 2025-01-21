def insertion_sort(arr):
    """
    Sorts an array using the Insertion Sort algorithm.
    Returns the sorted array.
    """
    n = len(arr)  # Get the length of the array
    
    if n <= 1:
        return arr  # If the array has 0 or 1 element, it is already sorted
    
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i - 1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j + 1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j + 1] = key  # Insert the key in the correct position
    
    return arr  # Return the sorted array
