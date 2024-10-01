def bubble_sort(arr: list[float]) -> list[float]:
    """Sort the array inplace and return it.

    >>> bubble_sort([5,3, 1])
    [1, 3, 5]
    >>> bubble_sort([1, 3, 5])
    [1, 3, 5]
    """
    n = len(arr)
    for first_n in range(n-1, 0, -1):
        for i in range(first_n):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr
