from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)

        for n in num_set:
            if n-1 not in num_set:
                lenght = 1
                while (n + lenght) in num_set:
                    lenght += 1
                longest = max(longest, lenght)
        return longest