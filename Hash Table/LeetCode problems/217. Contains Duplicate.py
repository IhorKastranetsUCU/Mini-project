from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashtable = {}
        for num in nums:
            count = hashtable.get(num, 0)
            if count == 1:
                return True
            hashtable[num] = 1 + count
        return False