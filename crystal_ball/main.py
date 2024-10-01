"""Very funny problem.
Given two crystal balls and N-story building,
find the point the first floor of breaking optimally.
"""


def crystal_ball(arr: list[bool]) -> int:
    """arr[i] = True if break on this floor

    >>> crystal_ball([False, False, True, True, True, True, True, True])
    2
    >>> crystal_ball([False, False])
    -1
    >>> crystal_ball([])
    -1
    >>> crystal_ball([True, True, True, True, True])
    0
    """
    n = len(arr)
    if n == 0:
        return -1
    if arr[0]:
        return 0

    n_sqrt = int(n**0.5)
    i = 0
    while i < n:
        if arr[i]:
            break
        i += n_sqrt
    i -= n_sqrt
    for i in range(i, n):
        if arr[i]:
            return i
    return -1
