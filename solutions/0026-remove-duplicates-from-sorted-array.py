"""
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

--------

Time:  O(n)  - one pass
Space: O(1)  - two variables, and the writes are in place


"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = nums[0]
        k = 1

        for num in nums:
            if temp != num:
                temp = num
                k += 1
                nums[k - 1] = num

        return k


if __name__ == "__main__":
    s = Solution()

    def run(nums):
        """Returns (k, the first k elements) so tests can check both."""
        arr = list(nums)
        k = s.removeDuplicates(arr)
        return k, arr[:k]

    assert run([1, 1, 2]) == (2, [1, 2])
    assert run([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == (5, [0, 1, 2, 3, 4])
    assert run([1]) == (1, [1])                      # edge: single element
    assert run([1, 2, 3]) == (3, [1, 2, 3])          # edge: no duplicates at all
    assert run([2, 2, 2, 2]) == (1, [2])             # edge: all identical
    assert run([-3, -3, -1, 0, 0, 5]) == (4, [-3, -1, 0, 5])   # edge: negatives

    # Property test: for any sorted input, the answer is sorted(set(input)).
    import random

    random.seed(0)
    for _ in range(10000):
        case = sorted(random.randint(0, 8) for _ in range(random.randint(1, 12)))
        expected = sorted(set(case))
        assert run(case) == (len(expected), expected), case

    print("all passed")