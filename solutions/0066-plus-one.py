"""
66. Plus One
https://leetcode.com/problems/plus-one/

Approach
--------
  - digit < 9  -> it can absorb the +1 without carrying. Increment, return.
  - digit == 9 -> adding one makes it 10: write 0 and carry left.

Time:  O(n)  - one pass, and it usually stops at the first digit
Space: O(1)  - in place, except the all-nines case, which must grow by one
-------
"""
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits


if __name__ == "__main__":
    s = Solution()

    assert s.plusOne([1, 2, 3]) == [1, 2, 4]
    assert s.plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert s.plusOne([0]) == [1]                    # edge: zero
    assert s.plusOne([9]) == [1, 0]                 # edge: single nine, grows
    assert s.plusOne([9, 9]) == [1, 0, 0]           # edge: all nines
    assert s.plusOne([9, 9, 9]) == [1, 0, 0, 0]
    assert s.plusOne([1, 9, 9]) == [2, 0, 0]        # edge: carry stops partway
    assert s.plusOne([8, 9, 9, 9]) == [9, 0, 0, 0]  # edge: carry stops at the first digit

    # Property test: the digit array IS a number, so compare against integer
    # arithmetic. Independent of the algorithm, which is what makes it useful.
    import random

    def reference(digits):
        n = int("".join(map(str, digits))) + 1
        return [int(c) for c in str(n)]

    random.seed(0)
    for _ in range(10000):
        length = random.randint(1, 8)
        case = [random.randint(0, 9) for _ in range(length)]
        if length > 1 and case[0] == 0:
            case[0] = random.randint(1, 9)      # no leading zeros, per constraints
        assert s.plusOne(list(case)) == reference(case), case

    print("all passed")