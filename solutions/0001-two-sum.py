"""
1. Two Sum
https://leetcode.com/problems/two-sum/

Approach: one pass, hash map of value -> index. For each x, look for its
complement (target - x) among the values already seen. Checking before
inserting is what stops an element pairing with itself.
Time: O(n)   Space: O(n)
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, x in enumerate(nums):
            if target - x in seen:
                return [seen[target - x], i]
            seen[x] = i
        return []


if __name__ == "__main__":
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]      # answer is not the first element
    assert s.twoSum([3, 3], 6) == [0, 1]         # edge: same value twice
    assert s.twoSum([1, 2], 99) == []            # edge: no solution
    print("all passed")
