class Solution(object):
    def singleNumber(self, nums):
        single = 0
        for num in nums:
            single ^= num
        return single
        """
        :type nums: List[int]
        :rtype: int
        """
        