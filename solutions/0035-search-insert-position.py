"""35. Search Insert Position  ·  https://leetcode.com/problems/search-insert-position/

COMPLEXITY
-----------------
Time:  O(log n)
Space: O(1).
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    def searchInsertHalving(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        diff = len(nums)

        if target > nums[right]:
            return right + 1

        while diff > 0:
            diff = (right - left + 1) // 2
            mid = (right + left) // 2

            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                left += diff
            else:
                right -= diff
        return mid


# ---------------------------------------------------------------- tests
def _reference(nums: list[int], target: int) -> int:
    """Independent and deliberately naive: first index whose value is >= target."""
    for i, v in enumerate(nums):
        if v >= target:
            return i
    return len(nums)


def _probes(nums: list[int], target: int, exclude_mid: bool) -> list[int]:
    """Replay either approach and record every index it looks at."""
    seen = []
    left, right = 0, len(nums) - 1
    if exclude_mid:
        while left <= right:
            mid = (left + right) // 2
            seen.append(mid)
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    else:
        diff = len(nums)
        if target > nums[right]:
            return seen
        while diff > 0:
            diff = (right - left + 1) // 2
            mid = (right + left) // 2
            seen.append(mid)
            if target == nums[mid]:
                break
            elif target > nums[mid]:
                left += diff
            else:
                right -= diff
    return seen


if __name__ == "__main__":
    import itertools
    import random

    sol = Solution()
    both = (sol.searchInsert, sol.searchInsertHalving)

    # 1. the examples from the problem
    for f in both:
        assert f([1, 3, 5, 6], 5) == 2
        assert f([1, 3, 5, 6], 2) == 1
        assert f([1, 3, 5, 6], 7) == 4

    # 2. edges: before everything, after everything, single element
    for f in both:
        assert f([1, 3, 5, 6], 0) == 0
        assert f([1, 3, 5, 6], 1) == 0
        assert f([1, 3, 5, 6], 6) == 3
        assert f([5], 5) == 0
        assert f([5], 1) == 0
        assert f([5], 9) == 1
        assert f([-10, -5, 0], -7) == 1

    # 3. empty array — only approach 2 handles it (LeetCode guarantees n >= 1)
    assert sol.searchInsert([], 3) == 0
    try:
        sol.searchInsertHalving([], 3)
        raise AssertionError("approach 1 was expected to raise on []")
    except IndexError:
        pass

    # 4. exhaustive: every sorted distinct array up to length 8, every target
    #    from below the minimum to above the maximum — 303,436 cases
    for n in range(1, 9):
        for combo in itertools.combinations(range(n * 2), n):
            arr = list(combo)
            for t in range(-1, n * 2 + 1):
                want = _reference(arr, t)
                assert sol.searchInsert(arr, t) == want, (arr, t)
                assert sol.searchInsertHalving(arr, t) == want, (arr, t)

    # 5. the duplicate-probe claim: approach 1 sometimes repeats, approach 2 never
    assert _probes([1, 3, 5, 7], 4, exclude_mid=False) == [1, 2, 2]
    repeats_1 = repeats_2 = 0
    for n in range(1, 9):
        for combo in itertools.combinations(range(n * 2), n):
            arr = list(combo)
            for t in range(-1, n * 2 + 1):
                p1 = _probes(arr, t, exclude_mid=False)
                p2 = _probes(arr, t, exclude_mid=True)
                repeats_1 += len(p1) != len(set(p1))
                repeats_2 += len(p2) != len(set(p2))
    assert repeats_1 > 0
    assert repeats_2 == 0

    # 6. O(log n), measured
    random.seed(0)
    for size in (1_000, 100_000):
        arr = list(range(0, 2 * size, 2))
        targets = [-1, 2 * size + 1] + [random.randint(-1, 2 * size) for _ in range(300)]
        limit = size.bit_length() + 1
        for t in targets:
            assert len(_probes(arr, t, exclude_mid=True)) <= limit, (size, t)
            assert len(_probes(arr, t, exclude_mid=False)) <= limit + 1, (size, t)

    print("all passed")