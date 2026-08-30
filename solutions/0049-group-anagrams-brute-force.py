"""
49. Group Anagrams  -  BRUTE FORCE (Time Limit Exceeded on submission)
https://leetcode.com/problems/group-anagrams/

Kept deliberately. This version is CORRECT but too slow, and the reason
why is the whole lesson of the problem.

Approach
--------
For each word that has not been grouped yet, create a new group for it,
then scan every later word and append the ones that are anagrams of it.
`seen` records words already placed so they never start a group of their
own. Anagram testing reuses the character-counting solution from 242.

Complexity
----------
Time:  O(n^2 * k)  - every pair of words is compared, and each comparison
                     builds two character maps over words of length k
Space: O(n * k)    - the groups, plus the two maps per comparison

Measured on random 8-letter words (all distinct - the worst case):

    n =  500     0.190 s
    n = 1000     0.772 s      <- double n, time x4
    n = 2000     3.087 s      <- double n, time x4 again

That x4 per doubling is the signature of O(n^2). Extrapolated to the
n = 10^4 the constraints allow, this is roughly 77 seconds against a
limit of a few - hence TLE.

`seen` does cut real work, but the inner loop still scans to the end, so
the shape stays quadratic. A constant-factor win never rescues the wrong
complexity class.

The bottleneck is comparing every PAIR. See 49-group-anagrams.py for the
linear version, which never compares two words at all: each word computes
its own sorted-letter fingerprint and drops into a bucket keyed by it.
"""
from typing import List


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

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = set()
        result = []
        setCounter = -1

        for i in range(len(strs)):
            if strs[i] not in seen:
                result.append([strs[i]])
                setCounter += 1

                for j in range(i + 1, len(strs)):
                    if self.isAnagram(strs[i], strs[j]):
                        seen.add(strs[j])
                        result[setCounter].append(strs[j])
        return result


if __name__ == "__main__":
    def norm(groups):
        """Group order and within-group order are not specified by the
        problem, so compare canonically."""
        return sorted(sorted(g) for g in groups)

    s = Solution()

    assert norm(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == \
        norm([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
    assert norm(s.groupAnagrams([""])) == [[""]]              # edge: empty string
    assert norm(s.groupAnagrams(["a"])) == [["a"]]            # edge: single word
    assert norm(s.groupAnagrams(["a", "a"])) == [["a", "a"]]  # edge: duplicates
    assert norm(s.groupAnagrams(["a", "b", "a"])) == norm([["a", "a"], ["b"]])
    assert norm(s.groupAnagrams(["ab", "ba", "abc"])) == norm([["ab", "ba"], ["abc"]])
    print("all passed")
