"""704. Binary Search  ·  https://leetcode.com/problems/binary-search/

COMPLEXITY
----------
Time:  O(log n)
Space: O(1)

"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        diff = len(nums)          # seeded only to enter the loop; see the docstring

        while diff > 0:
            mid = (left + right) // 2
            diff = (right - left + 1) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left += diff
            else:
                right -= diff

        return -1


# ---------------------------------------------------------------- tests
def _reference(nums: list[int], target: int) -> int:
    """Independent, deliberately naive. Never share logic with the thing you test."""
    for i, v in enumerate(nums):
        if v == target:
            return i
    return -1


if __name__ == "__main__":
    import itertools
    import random

    s = Solution()

    # 1. the examples from the problem
    assert s.search([-1, 0, 3, 5, 9, 12], 9) == 4
    assert s.search([-1, 0, 3, 5, 9, 12], 2) == -1

    # 2. edge cases
    assert s.search([], 1) == -1            # empty: right = -1, diff = 0, loop never runs
    assert s.search([5], 5) == 0            # single element, present
    assert s.search([5], 3) == -1           # single element, target smaller
    assert s.search([5], 7) == -1           # single element, target larger
    assert s.search([1, 2], 1) == 0         # two elements, both halves
    assert s.search([1, 2], 2) == 1
    assert s.search([-10, -5, -1], -10) == 0    # negatives, first
    assert s.search([-10, -5, -1], -1) == 2     # negatives, last

    # 3. exhaustive — every sorted array of distinct ints up to n = 8,
    #    every target inside and outside the range
    for n in range(1, 9):
        for combo in itertools.combinations(range(n * 2), n):
            arr = list(combo)
            for t in range(-1, n * 2 + 1):
                assert s.search(arr, t) == _reference(arr, t), (arr, t)

    # 4. property test against the reference at scale
    random.seed(0)
    for _ in range(2000):
        n = random.randint(1, 500)
        arr = sorted(random.sample(range(n * 4), n))
        t = random.choice(arr + [arr[0] - 1, arr[-1] + 1])
        assert s.search(arr, t) == _reference(arr, t), (arr, t)

    # 5. the O(log n) claim, actually measured rather than asserted
    def probes(arr: list[int], target: int) -> int:
        left, right, diff, n = 0, len(arr) - 1, len(arr), 0
        while diff > 0:
            n += 1
            mid = (left + right) // 2
            diff = (right - left + 1) // 2
            if arr[mid] == target:
                return n
            elif arr[mid] < target:
                left += diff
            else:
                right -= diff
        return n

    for size in (1_000, 10_000, 100_000):
        arr = list(range(size))
        worst = max(probes(arr, t) for t in (-1, 0, size // 3, size - 1, size))
        limit = size.bit_length() + 1          # ~log2(size) + 1
        assert worst <= limit, (size, worst, limit)

    print("all passed")