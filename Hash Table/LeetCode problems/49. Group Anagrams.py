from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}
        for item in strs:
            key = "".join(sorted(item))
            if key not in hashtable:
                hashtable[key] = []
            hashtable[key].append(item)
        ans = []
        for key in hashtable:
            ans.append(hashtable[key])
        return ans