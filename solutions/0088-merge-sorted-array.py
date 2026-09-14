"""
88. Merge Sorted Array
https://leetcode.com/problems/merge-sorted-array/

--------

Time:  O(m + n)  - each element is written exactly once
Space: O(1)      - two counters, all writes in place

"""
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """Do not return anything, modify nums1 in-place instead."""
        i = m
        j = n

        while j > 0:
            if i == 0:
                nums1[0:j] = nums2[0:j]
                break
            elif nums1[i - 1] >= nums2[j - 1]:
                nums1[i + j - 1] = nums1[i - 1]
                i -= 1
            else:
                nums1[i + j - 1] = nums2[j - 1]
                j -= 1


if __name__ == "__main__":
    s = Solution()

    def run(nums1, m, nums2, n):
        """merge returns None, so hand back the mutated nums1 for testing."""
        arr = list(nums1)
        s.merge(arr, m, list(nums2), n)
        return arr

    assert run([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3) == [1, 2, 2, 3, 5, 6]
    assert run([1], 1, [], 0) == [1]                       # edge: nums2 empty
    assert run([0], 0, [1], 1) == [1]                      # edge: nums1 empty
    assert run([2, 0], 1, [1], 1) == [1, 2]                # edge: nums1 exhausted first
    assert run([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3) == [1, 2, 3, 4, 5, 6]   # no interleaving
    assert run([0, 0, 0], 0, [1, 2, 3], 3) == [1, 2, 3]    # edge: m = 0
    assert run([5, 5, 0, 0], 2, [5, 5], 2) == [5, 5, 5, 5]  # edge: all ties
    assert run([-1, 3, 0, 0], 2, [-5, 0], 2) == [-5, -1, 0, 3]   # edge: negatives

    # Property test: the merge of two sorted lists is just sorted(a + b).
    import random

    random.seed(0)
    for _ in range(10000):
        m = random.randint(0, 5)
        n = random.randint(0, 5)
        a = sorted(random.randint(-9, 9) for _ in range(m))
        b = sorted(random.randint(-9, 9) for _ in range(n))
        assert run(a + [0] * n, m, b, n) == sorted(a + b), (a, b)

    print("all passed")