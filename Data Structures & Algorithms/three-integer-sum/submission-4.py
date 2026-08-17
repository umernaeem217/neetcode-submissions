class Solution:
    def pairSum(self, arr, l, target):
        pairs = []
        r = len(arr) - 1
        while l < r:
            s = arr[r]+ arr[l]
            if s < target:
                l+=1
            elif s > target:
                r-=1
            else:
                pairs.append([l , r])
                l+=1
                while l < r and arr[l] == arr[l-1]:
                    l+=1
        return pairs

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            pairs = self.pairSum(nums, i+1, -nums[i])
            for j, k in pairs:
                res.append([nums[i], nums[j], nums[k]])
        return res
            
