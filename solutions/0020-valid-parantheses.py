"""20. Valid Parentheses  · https://leetcode.com/problems/valid-parentheses/


COMPLEXITY
----------
Time:  O(n)  — one pass, O(1) work per character.
Space: O(n)
"""


class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        pair = {")": "(", "]": "[", "}": "{"}

        if len(s) % 2 == 1:
            return False

        for char in s:
            if char in "([{":
                st.append(char)
            elif len(st) == 0:
                return False
            elif char in pair:
                if st.pop() != pair[char]:
                    return False
        return len(st) == 0


# ---------------------------------------------------------------- tests
def _reference(s: str) -> bool:
    """Independent check: repeatedly strip innermost matched pairs; valid iff
    the string reduces to empty. No stack, so it can't share a bug with the
    solution above."""
    prev = None
    while prev != s:
        prev = s
        s = s.replace("()", "").replace("[]", "").replace("{}", "")
    return s == ""


if __name__ == "__main__":
    import itertools
    import random

    sol = Solution()

    # 1. the examples from the problem
    assert sol.isValid("()") is True
    assert sol.isValid("()[]{}") is True
    assert sol.isValid("(]") is False
    assert sol.isValid("([)]") is False
    assert sol.isValid("{[]}") is True

    # 2. edge cases
    assert sol.isValid("") is True                # empty string, vacuously valid
    assert sol.isValid("(") is False               # opener with nothing to close it
    assert sol.isValid(")") is False               # closer with nothing to pop
    assert sol.isValid("((") is False
    assert sol.isValid("))") is False
    assert sol.isValid("(((((((((") is False       # odd length, caught by the length check
    assert sol.isValid("()()()()") is True          # sequential, not nested
    assert sol.isValid("((()))") is True            # nested, not sequential
    assert sol.isValid("([{}])") is True             # all three types, nested

    # 3. exhaustive: every string up to length 8 over the 6 bracket characters
    #    (6**0 + 6**1 + ... + 6**8 = 2,015,539 strings)
    chars = "()[]{}"
    for n in range(9):
        for tup in itertools.product(chars, repeat=n):
            s = "".join(tup)
            assert sol.isValid(s) == _reference(s), s

    # 4. property test: valid strings built by construction (always balanced),
    #    up to length 200
    random.seed(0)

    def random_valid(n_pairs: int) -> str:
        opens = "([{"
        closes = {"(": ")", "[": "]", "{": "}"}
        out = []
        stack = []
        # at each step, either open a new bracket or close the innermost one
        remaining_opens = n_pairs
        while remaining_opens > 0 or stack:
            if remaining_opens > 0 and (not stack or random.random() < 0.5):
                o = random.choice(opens)
                out.append(o)
                stack.append(o)
                remaining_opens -= 1
            else:
                out.append(closes[stack.pop()])
        return "".join(out)

    for _ in range(20_000):
        s = random_valid(random.randint(0, 100))
        assert sol.isValid(s) is True, s
        assert _reference(s) is True, s

    # 5. property test: pure noise, mostly invalid, checked against the
    #    independent reference rather than an assumed answer
    for _ in range(20_000):
        n = random.randint(0, 200)
        s = "".join(random.choice(chars) for _ in range(n))
        assert sol.isValid(s) == _reference(s), s

    # 6. a valid string with one character flipped is (almost always) invalid —
    #    sanity check that the solution isn't accidentally permissive
    flips_checked = 0
    for _ in range(5_000):
        s = random_valid(random.randint(1, 30))
        if not s:
            continue
        i = random.randrange(len(s))
        other = random.choice([c for c in chars if c != s[i]])
        flipped = s[:i] + other + s[i + 1:]
        assert sol.isValid(flipped) == _reference(flipped), (s, i, flipped)
        flips_checked += 1
    assert flips_checked > 0

    print("all passed")