class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for num in nums:
            if num - 1 not in s:
                ans = 0 
                while num in s:
                    num+=1
                    ans+=1
                res = max(res, ans)
        return res