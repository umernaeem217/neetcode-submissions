class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        c1 = Counter(s)
        c2 = Counter(t)

        for key, value in c1.items():
            if key not in c2:
                return False
            if c2[key] != value:
                return False
        
        for key, value in c2.items():
            if key not in c1:
                return False
            if c1[key] != value:
                return False
        return True
            