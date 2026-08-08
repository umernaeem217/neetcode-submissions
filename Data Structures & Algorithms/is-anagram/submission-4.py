from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort and compare, Time = (n log n), Space: O(1)
        # s = ''.join(sorted(s))
        # t = ''.join(sorted(t))
        # return s == t
        c1 = Counter(s)
        c2 = Counter(t)
        return c1 == c2
