"""
169. Majority Element
https://leetcode.com/problems/majority-element/

Approach
--------

Time:  O(n)  - one pass
Space: O(n)  - the dictionary

"""
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        seen = {}

        for num in nums:
            if num in seen:
                seen[num] += 1
                if seen[num] >= (len(nums) / 2):
                    return num
            else:
                seen[num] = 1

        return max(seen, key=seen.get)


if __name__ == "__main__":
    s = Solution()

    assert s.majorityElement([3, 2, 3]) == 3
    assert s.majorityElement([2, 2, 1, 1, 1, 2, 2]) == 2
    assert s.majorityElement([1]) == 1                   # edge: single element
    assert s.majorityElement([1, 1]) == 1                # edge: all the same
    assert s.majorityElement([5, 5, 5, 9]) == 5          # edge: majority first
    assert s.majorityElement([9, 5, 5, 5]) == 5          # edge: majority last
    assert s.majorityElement([-1, -1, 2]) == -1          # edge: negatives
    assert s.majorityElement([0, 0, 1]) == 0             # edge: zero as the answer

    import random

    random.seed(0)
    for _ in range(10000):
        n = random.randint(1, 15)
        majority = random.randint(-9, 9)
        others = [x for x in range(-9, 10) if x != majority]
        case = [majority] * (n // 2 + 1)
        case += [random.choice(others) for _ in range(n - len(case))]
        random.shuffle(case)
        assert s.majorityElement(case) == majority, case

    print("all passed")