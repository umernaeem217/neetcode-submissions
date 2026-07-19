class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in s:
            c = 0
            while num in s:
                num = num +1
                c+=1
            res = max(res, c)
        return res