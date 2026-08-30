"""
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

Complexity
----------
Time:  O(n^2 * k log k) worst case  - every pair is considered, and each
                                      surviving pair sorts two words of
                                      length k
Space: O(n * k)                     - every input word appears in exactly
                                      one group, once

Note on the acceptance
----------------------
This is accepted, but the length filter is doing the work. When words
have varied lengths (as the real test data does) it rejects the large
majority of pairs; when they do not, the filter never fires and the
quadratic shape is exposed. Measured on n = 10,000 random words:

    varied lengths (like the real tests)     5.6 s
    all words the same length (worst case)  43.0 s

So this passes because of a property of the input, not of the algorithm.
The linear alternative avoids pair comparison entirely: give each word a
fingerprint - its letters in sorted order - and bucket words by it in a
dict, one pass, O(n * k log k).
"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        seen = set()
        counter = 0
        for i in range(len(strs)):
            if strs[i] not in seen:
                result.append([strs[i]])
                seen.add(strs[i])
                counter += 1
                for j in range(i + 1, len(strs)):
                    if len(strs[j]) == len(strs[i]):
                        if sorted(strs[i]) == sorted(strs[j]):
                            result[counter - 1].append(strs[j])
                            seen.add(strs[j])
        return result


if __name__ == "__main__":
    def norm(groups):
        """Neither group order nor order within a group is specified by the
        problem, so compare canonically."""
        return sorted(sorted(g) for g in groups)

    s = Solution()

    assert norm(s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])) == \
        norm([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
    assert norm(s.groupAnagrams([""])) == [[""]]                      # edge: empty string
    assert norm(s.groupAnagrams(["a"])) == [["a"]]                    # edge: single word
    assert norm(s.groupAnagrams(["a", "a"])) == [["a", "a"]]          # edge: duplicates
    assert norm(s.groupAnagrams(["a", "b", "a"])) == norm([["a", "a"], ["b"]])
    assert norm(s.groupAnagrams(["ab", "ba", "abc"])) == norm([["ab", "ba"], ["abc"]])
    assert norm(s.groupAnagrams(["abc", "bca", "cab"])) == [["abc", "bca", "cab"]]
    print("all passed")
