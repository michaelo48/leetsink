class Solution(object):
    def search(self, nums, target):
        L = 0
        R = len(nums)-1
        
        while L <= R:
            M = (L + R)//2
            if nums[M] == target:
                return M
            elif nums[M] > target:
                R = M - 1
            else:
                L = M + 1
        return -1
            

        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        