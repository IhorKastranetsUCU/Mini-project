class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ans = 0
        cur_count = 0
        for num in nums:
            if num == 1:
                cur_count += 1
                ans = max(cur_count, ans)
            else:
                cur_count = 0
        return ans