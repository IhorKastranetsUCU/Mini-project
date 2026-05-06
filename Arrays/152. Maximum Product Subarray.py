class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        cur_min, cur_max = 1, 1
        n = len(nums)
        for i in range(n):
            tmp = cur_max
            cur_max = max(nums[i] * tmp, nums[i], cur_min*nums[i])
            cur_min = min(nums[i], tmp * nums[i], cur_min*nums[i])
            ans = max(cur_max, ans)
        return ans