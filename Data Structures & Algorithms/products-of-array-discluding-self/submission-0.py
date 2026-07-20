class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            agg = 1
            for j in range(len(nums)):
                if i != j:
                    agg*= nums[j]
            res.append(agg)
        return res