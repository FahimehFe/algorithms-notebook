"""278. First Bad Version  ·  https://leetcode.com/problems/first-bad-version/

COMPLEXITY (both)
-----------------
Time:  O(log n) API calls.   Space: O(1).
"""
from collections.abc import Callable

isBadVersion: Callable[[int], bool] = lambda version: False  # noqa: E731


class Solution:
    def firstBadVersion(self, n: int) -> int:
        """Approach 2 — lower bound. Never asks about the same version twice."""
        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2
            if isBadVersion(mid):
                right = mid          # mid might BE the first bad one — keep it
            else:
                left = mid + 1       # mid is good, so the answer is after it
        return left

    def firstBadVersionHalving(self, n: int) -> int:
        """Approach 1 — my halving-by-width version. Correct; sometimes repeats a call."""
        left = 1
        right = n
        diff = n

        while diff > 0:
            diff = (right - left + 1) // 2
            mid = (right + left) // 2
            isBad = isBadVersion(mid)

            if isBad:
                right -= diff
            else:
                left += diff
        return mid


# ---------------------------------------------------------------- tests
def _install_api(first_bad: int) -> list[int]:
    """Install a fake isBadVersion for one case; return the list it logs calls to."""
    calls: list[int] = []

    def api(version: int) -> bool:
        calls.append(version)
        return version >= first_bad

    globals()["isBadVersion"] = api
    return calls


if __name__ == "__main__":
    import math
    import random

    sol = Solution()

    # 1. examples from the problem
    for method in (sol.firstBadVersion, sol.firstBadVersionHalving):
        _install_api(4)
        assert method(5) == 4
        _install_api(1)
        assert method(1) == 1

    # 2. the repeated-call example, and the fix
    calls = _install_api(1)
    assert sol.firstBadVersionHalving(2) == 1
    assert calls == [1, 1]                      # asked about version 1 twice
    calls = _install_api(1)
    assert sol.firstBadVersion(2) == 1
    assert calls == [1]                         # once

    # 3. exhaustive: every (n, first bad) pair up to n = 200 — 20,100 cases
    for n in range(1, 201):
        for bad in range(1, n + 1):
            calls = _install_api(bad)
            assert sol.firstBadVersion(n) == bad, (n, bad)
            assert len(calls) == len(set(calls)), (n, bad, calls)     # no repeats
            assert len(calls) <= math.ceil(math.log2(n)), (n, bad, calls)
            _install_api(bad)
            assert sol.firstBadVersionHalving(n) == bad, (n, bad)

    # 4. LeetCode's full range: n up to 2**31 - 1
    random.seed(0)
    for _ in range(5_000):
        n = random.randint(1, 2**31 - 1)
        bad = random.randint(1, n)
        calls = _install_api(bad)
        assert sol.firstBadVersion(n) == bad
        assert len(calls) <= 31
        assert len(calls) == len(set(calls))
        _install_api(bad)
        assert sol.firstBadVersionHalving(n) == bad

    # 5. extremes of the range
    for bad in (1, 2, 2**31 - 2, 2**31 - 1):
        _install_api(bad)
        assert sol.firstBadVersion(2**31 - 1) == bad
        _install_api(bad)
        assert sol.firstBadVersionHalving(2**31 - 1) == bad

    print("all passed")