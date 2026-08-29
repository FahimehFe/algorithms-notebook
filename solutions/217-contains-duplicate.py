"""
217. Contains Duplicate
https://leetcode.com/problems/contains-duplicate/

Approach: one pass, hash set. Check membership before inserting,
return early on the first repeat.
Time: O(n)   Space: O(n)
"""

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False


if __name__ == "__main__":
    s = Solution()
    assert s.containsDuplicate([1, 2, 3, 1]) is True
    assert s.containsDuplicate([1, 2, 3]) is False
    assert s.containsDuplicate([]) is False      # edge: empty
    assert s.containsDuplicate([1]) is False     # edge: single
    print("all passed")
