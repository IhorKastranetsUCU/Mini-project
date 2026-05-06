class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        maxval = [0, 0]

        for num, frequency in count.items():
            if frequency > maxval[1]:
                maxval[0] = num
                maxval[1] = frequency

        return maxval[0]