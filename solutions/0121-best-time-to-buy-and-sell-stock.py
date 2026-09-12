"""
121. Best Time to Buy and Sell Stock
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


Time:  O(n)  - one pass
Space: O(1)  - two integers

----------------------------------
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        diff = 0

        for price in prices:
            if (price - buy) > diff:
                diff = price - buy
            elif price < buy:
                buy = price

        return diff


if __name__ == "__main__":
    s = Solution()

    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0     # edge: only losses -> 0, never negative
    assert s.maxProfit([1]) == 0                 # edge: single day, no trade possible
    assert s.maxProfit([2, 4, 1]) == 2           # edge: the ordering trap
    assert s.maxProfit([3, 1, 4]) == 3           # edge: minimum in the middle
    assert s.maxProfit([3, 3, 3]) == 0           # edge: all equal
    assert s.maxProfit([10000, 0, 10000]) == 10000

    # Property test against an obvious reference implementation.
    import random

    def reference(prices):
        lowest, best = prices[0], 0
        for p in prices:
            lowest = min(lowest, p)
            best = max(best, p - lowest)
        return best

    random.seed(0)
    for _ in range(10000):
        case = [random.randint(0, 30) for _ in range(random.randint(1, 12))]
        assert s.maxProfit(case) == reference(case), case

    print("all passed")