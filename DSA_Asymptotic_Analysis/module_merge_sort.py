# merge_sort_module.py

def merge_sort(arr):
    """
    Sorts an array using the Merge Sort algorithm.
    """
    # Base case: If the list has one element, it's already sorted
    if len(arr) <= 1:
        return arr
    # Split the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursively split and merge the halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the two sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    """
    Merges two sorted arrays into one sorted array.
    """
    sorted_arr = []
    while left and right:
        if left[0] < right[0]:
            sorted_arr.append(left.pop(0))
        else:
            sorted_arr.append(right.pop(0))
    
    # Add remaining elements (if any)
    sorted_arr.extend(left)
    sorted_arr.extend(right)
    
    return sorted_arr
