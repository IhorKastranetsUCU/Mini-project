from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            firstElement = nums[i]
            target = 0 - firstElement

            pairs = self.twoSum(nums, i + 1, n - 1, target)

            for pair in pairs:
                triplet = [firstElement, pair[0], pair[1]]
                ans.append(triplet)

        return ans

    def twoSum(self, nums: List[int], start: int, end: int, target: int) -> List[List[int]]:
        f = start
        s = end
        pairs = []

        while f < s:
            if f > start and nums[f] == nums[f - 1]:
                f += 1
                continue

            if s < end and nums[s] == nums[s + 1]:
                s -= 1
                continue

            current_sum = nums[f] + nums[s]

            if current_sum < target:
                f += 1
            elif current_sum > target:
                s -= 1
            else:
                pairs.append([nums[f], nums[s]])
                f += 1
                s -= 1

        return pairs