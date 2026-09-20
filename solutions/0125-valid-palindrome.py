"""125. Valid Palindrome  ·  https://leetcode.com/problems/valid-palindrome/


                                   Time      Space
    1  clean a copy, compare       O(n)      O(n)
    2  two pointers from the ends  O(n)      O(1)
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """Approach 2 — two pointers, O(n) time, O(1) space."""
        left = 0
        right = len(s) - 1

        while left < right:
            while (not s[left].isalnum()) and (left < len(s) - 1):
                left += 1
            while (not s[right].isalnum()) and (right > 0):
                right -= 1

            if (not s[left].isalnum()) or (not s[right].isalnum()):
                break

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

    def isPalindromeCleanCopy(self, s: str) -> bool:
        """Approach 1 — clean a copy first. O(n) time, O(n) space."""
        s = s.lower()
        s = "".join(char for char in s if char.isalnum())

        for i in range(len(s) // 2):
            if s[i] != s[len(s) - 1 - i]:
                return False
        return True


# ---------------------------------------------------------------- tests
def _reference(s: str) -> bool:
    """Independent and deliberately naive. Never share logic with what you test."""
    cleaned = [ch for ch in s.lower() if ch.isalnum()]
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    import itertools
    import random
    import string
    import tracemalloc

    sol = Solution()
    both = (sol.isPalindrome, sol.isPalindromeCleanCopy)

    # 1. the examples from the problem
    for f in both:
        assert f("A man, a plan, a canal: Panama") is True
        assert f("race a car") is False
        assert f(" ") is True

    # 2. the edge cases from the docstring
    for f in both:
        assert f("") is True
        assert f(".,") is True
        assert f("0P") is False

    # 3. odd and even lengths, punctuation, digits
    for f in both:
        assert f("a") is True
        assert f("aa") is True
        assert f("ab") is False
        assert f("aba") is True
        assert f("abba") is True
        assert f("abca") is False
        assert f("ab_a") is True
        assert f("12321") is True
        assert f("1a2") is False
        assert f("...a...") is True          # one alnum, buried
        assert f("_ ,.!?") is True           # no alnum at all

    # 4. exhaustive: every string up to length 8 over an alphabet mixing upper,
    #    lower, digit and punctuation — 488,281 strings, both approaches
    for n in range(9):
        for tup in itertools.product("aA.b1", repeat=n):
            t = "".join(tup)
            want = _reference(t)
            assert sol.isPalindrome(t) == want, repr(t)
            assert sol.isPalindromeCleanCopy(t) == want, repr(t)

    # 5. property test at larger lengths, wider alphabet
    random.seed(0)
    alphabet = string.ascii_letters + string.digits + " .,:_-!?@#"
    for _ in range(200_000):
        t = "".join(random.choice(alphabet) for _ in range(random.randint(0, 16)))
        want = _reference(t)
        assert sol.isPalindrome(t) == want, repr(t)
        assert sol.isPalindromeCleanCopy(t) == want, repr(t)

    # 6. the O(1) space claim, measured rather than asserted: peak extra memory
    #    must not grow with the input
    peaks = []
    for size in (100_000, 400_000, 1_600_000):
        big = " ".join("abcBA" * (size // 5))
        tracemalloc.start()
        sol.isPalindrome(big)
        peaks.append(tracemalloc.get_traced_memory()[1])
        tracemalloc.stop()
    assert max(peaks) < 100 * 1024, peaks        # flat, and tiny, at every size
    assert max(peaks) < 4 * min(peaks), peaks    # not growing with n

    print("all passed")
