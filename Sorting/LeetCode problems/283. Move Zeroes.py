class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r = 0
        l = 0

        ans = len(nums) * [None]
        for i in range(len(nums)):
            if nums[i] != 0:
                ans[l] = nums[i]
                l += 1
            else:
                ans[len(nums) - r - 1] = 0
                r += 1

        for i in range(len(nums)):
            nums[i] = ans[i]


class Solution:
    def moveZeroes(self, nums):
        left = 0

        for right in range(len(nums)):

            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1