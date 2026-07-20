class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        post = [1] * len(nums)
        pre = [1] * len(nums)

        for i in range(1, len(nums)):
            pre[i] = pre[i-1] * nums[i-1]

        for i in range(len(nums)-2, -1, -1):
            post[i] = post[i+1] * nums[i+1]
        print(pre, post)
        for i in range(len(nums)):
            nums[i] = pre[i] * post[i]
        return nums