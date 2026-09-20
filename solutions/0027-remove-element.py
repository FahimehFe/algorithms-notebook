"""27. Remove Element  ·  https://leetcode.com/problems/remove-element/


COMPLEXITY
----------
Time:  O(n)
Space: O(1)

"""


class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                k += 1
            else:
                nums[i - k] = nums[i]

        return len(nums) - k


# ---------------------------------------------------------------- tests
if __name__ == "__main__":
    import itertools
    import random
    from collections import Counter

    sol = Solution()

    def check(original: list[int], val: int) -> None:
        """Check the LeetCode contract, not just the return value."""
        expected = [x for x in original if x != val]
        nums = list(original)
        k = sol.removeElement(nums, val)
        assert k == len(expected), (original, val, k, len(expected))
        # the judge only requires the right multiset in the first k slots
        assert Counter(nums[:k]) == Counter(expected), (original, val, nums[:k])
        # this solution also preserves order — assert the stronger property
        assert nums[:k] == expected, (original, val, nums[:k], expected)

    # 1. the examples from the problem
    check([3, 2, 2, 3], 3)
    check([0, 1, 2, 2, 3, 0, 4, 2], 2)

    # 2. edge cases
    check([], 0)                 # empty input
    check([1], 1)                # single element, removed
    check([1], 2)                # single element, kept
    check([2, 2, 2, 2], 2)       # everything removed -> k = 0
    check([1, 2, 3, 4], 9)       # nothing removed -> k = n, all writes are no-ops
    check([2, 1, 1, 1], 2)       # removal at the front
    check([1, 1, 1, 2], 2)       # removal at the back
    check([2, 1, 2, 1, 2], 2)    # alternating

    # 3. exhaustive: every array up to length 7 over {0,1,2}, every val in 0..3
    for n in range(8):
        for tup in itertools.product(range(3), repeat=n):
            for v in range(4):
                check(list(tup), v)

    # 4. property test at larger sizes, including values absent from the array
    random.seed(0)
    for _ in range(50_000):
        n = random.randint(0, 40)
        arr = [random.randint(0, 5) for _ in range(n)]
        check(arr, random.randint(0, 7))

    # 5. the invariant itself: the write index never runs ahead of the read index
    for _ in range(2_000):
        arr = [random.randint(0, 3) for _ in range(random.randint(0, 30))]
        v = random.randint(0, 3)
        k = 0
        for i in range(len(arr)):
            if arr[i] == v:
                k += 1
            else:
                assert i - k <= i, (arr, v, i, k)

    print("all passed")
