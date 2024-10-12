class Solution(object):
    def findPeakElement(self, nums):
        left, right = 0, len(nums) - 1
    
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[mid + 1]:
                right = mid  # Potential peak on the left side or at mid
            else:
                left = mid + 1  # Peak must be on the right side
            
        return left  # left == right, pointing to the peak element