"""
242. Valid Anagram
https://leetcode.com/problems/valid-anagram/

Approach: count each character of both strings into its own hash map,
then compare the two maps. Two strings are anagrams exactly when they
contain the same characters with the same counts, so dict equality is
the whole test.

Time:  O(n)  - one pass over each string
Space: O(1)  - the inputs are lowercase English letters, so each map
               holds at most 26 keys regardless of how long n gets

Note: sorting both strings and comparing also works, but that is
O(n log n). Counting is the reason this is linear.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = {}
        t_hash = {}
        for i in range(len(s)):
            if s[i] in s_hash:
                s_hash[s[i]] += 1
            else:
                s_hash[s[i]] = 1
        for i in range(len(t)):
            if t[i] in t_hash:
                t_hash[t[i]] += 1
            else:
                t_hash[t[i]] = 1
        return t_hash == s_hash


if __name__ == "__main__":
    s = Solution()
    assert s.isAnagram("anagram", "nagaram") is True
    assert s.isAnagram("rat", "car") is False
    assert s.isAnagram("ab", "ba") is True
    assert s.isAnagram("a", "ab") is False       # edge: different lengths
    assert s.isAnagram("a", "aa") is False       # edge: same letter, different count
    assert s.isAnagram("aab", "abb") is False    # edge: same letters, counts differ
    assert s.isAnagram("", "") is True           # edge: both empty
    print("all passed")
