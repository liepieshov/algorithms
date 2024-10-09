"""Implementation deatils.

Always remember that [left, right). Low inclusive, high exclusive.
Then you always round to floor divide.
Then when we update left we add +1 and when we update right, we just
use mid, because is always exclusive.

And for choosing left insertion or right insertion remember where
the equality goes.
"""
def binary_search(arr: list[float], value: float) -> int:
    """Binary search insertion point: arr[:idx] < value and arr[idx:] >= value

    >>> binary_search([1, 2, 3], 4)
    3
    >>> binary_search([1, 2, 3], 3)
    2
    >>> binary_search([1, 2, 3, 3], 3)
    2
    >>> binary_search([3, 3], 3)
    0
    >>> binary_search([3, 3], 2)
    0
    >>> binary_search([3, 3], 4)
    2
    >>> binary_search([3, 4], 3.5)
    1
    >>> binary_search_right([], 3.5)
    0
    """
    left = 0
    right = len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] >= value:
            right = mid
        else:
            left = mid + 1
    return left


def binary_search_right(arr: list[float], value: float) -> int:
    """Binary search insertion point: arr[:idx] <= value and arr[idx:] > value

    >>> binary_search_right([1, 2, 3], 4)
    3
    >>> binary_search_right([1, 2, 3], 3)
    3
    >>> binary_search_right([1, 2, 3, 3], 3)
    4
    >>> binary_search_right([3, 3], 3)
    2
    >>> binary_search_right([3, 3], 2)
    0
    >>> binary_search_right([3, 3], 4)
    2
    >>> binary_search_right([3, 4], 3.5)
    1
    >>> binary_search_right([], 3.5)
    0
    """
    left = 0
    right = len(arr)
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > value:
            right = mid
        else:
            left = mid + 1
    return left
