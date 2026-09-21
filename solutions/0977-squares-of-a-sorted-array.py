"""977. Squares of a Sorted Array  ·  https://leetcode.com/problems/squares-of-a-sorted-array/
O(n) time.
Space O(n)

"""


class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        """Approach 2 — two pointers, fill from the back. O(n)."""
        result = [0] * len(nums)
        left = 0
        right = len(nums) - 1

        for i in range(len(nums) - 1, -1, -1):
            a = nums[left] * nums[left]
            b = nums[right] * nums[right]
            if a > b:
                result[i] = a
                left += 1
            else:
                result[i] = b
                right -= 1
        return result

    def sortedSquaresOneLiner(self, nums: list[int]) -> list[int]:
        """Approach 1 — the baseline. Faster in CPython; see the docstring."""
        return sorted(x * x for x in nums)


# ---------------------------------------------------------------- tests
def _reference(nums: list[int]) -> list[int]:
    """Independent: square everything, sort with a simple insertion sort."""
    out: list[int] = []
    for x in nums:
        sq = x * x
        j = len(out)
        out.append(sq)
        while j > 0 and out[j - 1] > sq:
            out[j] = out[j - 1]
            j -= 1
        out[j] = sq
    return out


if __name__ == "__main__":
    import itertools
    import random

    sol = Solution()
    both = (sol.sortedSquares, sol.sortedSquaresOneLiner)

    # 1. the examples from the problem
    for f in both:
        assert f([-4, -1, 0, 3, 10]) == [0, 1, 9, 16, 100]
        assert f([-7, -3, 2, 3, 11]) == [4, 9, 9, 49, 121]

    # 2. edges: all negative, all positive, single, zeros, ties across zero
    for f in both:
        assert f([]) == []
        assert f([5]) == [25]
        assert f([-5]) == [25]
        assert f([0]) == [0]
        assert f([-3, -2, -1]) == [1, 4, 9]
        assert f([1, 2, 3]) == [1, 4, 9]
        assert f([-1, 1]) == [1, 1]
        assert f([-2, -2, 2, 2]) == [4, 4, 4, 4]
        assert f([-3, 0, 3]) == [0, 9, 9]
        assert f([0, 0, 0]) == [0, 0, 0]

    # 3. the first wrong attempt's failure case, kept as a regression test
    assert sol.sortedSquares([-4, -1, 0, 3, 10]) != [0, 0, 0, 9, 100]

    # 4. exhaustive: every sorted array (duplicates allowed) up to length 8
    #    over values -5..5 — 75,582 arrays
    for n in range(9):
        for tup in itertools.combinations_with_replacement(range(-5, 6), n):
            want = _reference(list(tup))
            assert sol.sortedSquares(list(tup)) == want, tup
            assert sol.sortedSquaresOneLiner(list(tup)) == want, tup

    # 5. property test over LeetCode's full value range
    random.seed(0)
    for _ in range(50_000):
        arr = sorted(random.randint(-10**4, 10**4) for _ in range(random.randint(0, 60)))
        want = _reference(arr)
        assert sol.sortedSquares(arr) == want
        assert sol.sortedSquaresOneLiner(arr) == want

    # 6. the input is not mutated
    original = [-4, -1, 0, 3, 10]
    snapshot = list(original)
    sol.sortedSquares(original)
    assert original == snapshot

    print("all passed")