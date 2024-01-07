class Solution(object):
    def containsDuplicate(self, nums):
        number = {}
        for num in nums:
            if num in number:
                return True
            number[num] = num
        return False
        