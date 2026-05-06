class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cursum = 0
        for i in range(len(nums)):
            cursum += nums[i]
            if cursum > ans:
                ans = cursum
            if cursum<0:
                cursum=0
        return ans