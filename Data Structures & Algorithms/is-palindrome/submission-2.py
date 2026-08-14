class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for c in s:
            if c.isalnum():
                arr.append(c.lower())
        l = 0
        r = len(arr) -1
        while l < r:
            if arr[l] != arr[r]:
                return False
            l+=1
            r-=1
        return True