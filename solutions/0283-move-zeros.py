"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/

--------

Time:  O(n)  - one pass 
Space: O(1)  - one counter;

"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """Do not return anything, modify nums in-place instead."""
        count_of_zeros = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                count_of_zeros += 1
            else:
                nums[i - count_of_zeros] = nums[i]

        nums[len(nums) - count_of_zeros:] = [0] * count_of_zeros


if __name__ == "__main__":
    s = Solution()

    def run(nums):
        """moveZeroes returns None, so hand back the mutated list for testing."""
        arr = list(nums)
        s.moveZeroes(arr)
        return arr

    assert run([0, 1, 0, 3, 12]) == [1, 3, 12, 0, 0]
    assert run([0]) == [0]                              # edge: single zero
    assert run([0, 0, 0]) == [0, 0, 0]                  # edge: all zeros
    assert run([1, 2, 3]) == [1, 2, 3]                  # edge: no zeros at all
    assert run([]) == []                                # edge: empty
    assert run([0, 1]) == [1, 0]                        # edge: leading zero
    assert run([-1, 0, -2, 0, 0, 3]) == [-1, -2, 3, 0, 0, 0]   # edge: negatives

    # Property test against an obviously-correct reference.
    import random

    def reference(nums):
        non_zeros = [x for x in nums if x != 0]
        return non_zeros + [0] * (len(nums) - len(non_zeros))

    random.seed(0)
    for _ in range(10000):
        case = [random.choice([0, 0, 1, 2, -3, 7]) for _ in range(random.randint(0, 12))]
        assert run(case) == reference(case), case

    print("all passed")