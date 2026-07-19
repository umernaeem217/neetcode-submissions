class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c1 = Counter(s)
        c2 = Counter(t)

        for c in c1.keys():
            if c1[c] != c2[c]:
                return False
        
        for c in c2.keys():
            if c2[c] != c1[c]:
                return False
        return True