from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort and compare, Time = (n log n), Space: O(1)
        # s = ''.join(sorted(s))
        # t = ''.join(sorted(t))
        # return s == t
        c1 = Counter(s)
        c2 = Counter(t)
        for key, value in c1.items():
            if key not in c2:
                return False
            if value != c2[key]:
                return False
        for key, value in c2.items():
            if key not in c1:
                return False
            if value != c1[key]:
                return False
        return True
