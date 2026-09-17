"""
724. Find Pivot Index
https://leetcode.com/problems/find-pivot-index/

--------

Time:  O(n)  - one pass for the total, one to scan
Space: O(1)  - two integers

"""
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        sumL = 0

        for i in range(len(nums)):
            if (total - nums[i] - sumL) == sumL:
                return i
            sumL += nums[i]

        return -1


if __name__ == "__main__":
    s = Solution()

    assert s.pivotIndex([1, 7, 3, 6, 5, 6]) == 3
    assert s.pivotIndex([1, 2, 3]) == -1               # edge: no pivot exists
    assert s.pivotIndex([2, 1, -1]) == 0               # edge: pivot at index 0
    assert s.pivotIndex([1]) == 0                      # edge: single element
    assert s.pivotIndex([0]) == 0
    assert s.pivotIndex([]) == -1                      # edge: empty
    assert s.pivotIndex([0, 0, 0]) == 0                # edge: all zeros, first match wins
    assert s.pivotIndex([1, -1]) == -1
    assert s.pivotIndex([-1, -1, -1, 0, 1, 1]) == 0    # edge: negatives
    assert s.pivotIndex([2, -2, 2]) == 0

    # Property test against a slow, obviously-correct reference: for each index,
    # actually slice and sum both sides. O(n^2) and irrelevant here - the point
    # is that it shares no reasoning with the solution above.
    import random

    def reference(nums):
        for i in range(len(nums)):
            if sum(nums[:i]) == sum(nums[i + 1:]):
                return i
        return -1

    random.seed(0)
    for _ in range(10000):
        case = [random.randint(-4, 4) for _ in range(random.randint(0, 10))]
        assert s.pivotIndex(case) == reference(case), case

    print("all passed")