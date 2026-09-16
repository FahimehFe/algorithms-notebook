"""
1480. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/

Approach
--------

Time:  O(n)  - one pass
Space: O(n)

"""
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)
        result[0] = nums[0]

        for i in range(1, len(nums)):
            result[i] = result[i - 1] + nums[i]

        return result


if __name__ == "__main__":
    s = Solution()

    assert s.runningSum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert s.runningSum([1, 1, 1, 1, 1]) == [1, 2, 3, 4, 5]
    assert s.runningSum([3, 1, 2, 10, 1]) == [3, 4, 6, 16, 17]
    assert s.runningSum([5]) == [5]                     # edge: single element
    assert s.runningSum([-1, -2, -3]) == [-1, -3, -6]   # edge: all negative
    assert s.runningSum([0, 0, 0]) == [0, 0, 0]         # edge: all zeros
    assert s.runningSum([5, -5, 5, -5]) == [5, 0, 5, 0]  # edge: cancelling

    import itertools
    import random

    random.seed(0)
    for _ in range(10000):
        case = [random.randint(-10, 10) for _ in range(random.randint(1, 12))]
        assert s.runningSum(list(case)) == list(itertools.accumulate(case)), case

    # The property that makes prefix sums useful: range sums in O(1).
    for _ in range(2000):
        case = [random.randint(-10, 10) for _ in range(random.randint(1, 12))]
        prefix = s.runningSum(list(case))
        i = random.randrange(len(case))
        j = random.randrange(i, len(case))
        expected = sum(case[i:j + 1])
        got = prefix[j] - (prefix[i - 1] if i > 0 else 0)
        assert got == expected, (case, i, j)

    print("all passed")