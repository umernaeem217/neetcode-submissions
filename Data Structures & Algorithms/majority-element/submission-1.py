class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        maxValue = float('-inf')
        res = 0
        for key, value in counter.items():
            if maxValue <= value:
                res = key
                maxValue = value
        return res