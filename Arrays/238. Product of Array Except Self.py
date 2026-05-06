class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_0 = 1
        zero_count = 0
        for i in range(len(nums)):
            if nums[i]:
                product_0 *= nums[i]
            else:
                zero_count += 1
        if zero_count >= 2:
            return [0] * len(nums)

        ans = [None] * len(nums)
        for i in range(len(nums)):
            if zero_count == 1:
                if nums[i] == 0:
                    ans[i] = product_0
                else:
                    ans[i] = 0
            else:
                ans[i] = product_0 // nums[i]
        return ans