class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k%len(nums)
        ans = [None] * len(nums)
        for i in range(len(nums)):
            ans[(k+i)%len(nums)] = nums[i]
        for i in range(len(nums)):
            nums[i] = ans[i]