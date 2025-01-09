class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        numies1 = []
        numies2 = []
        for n in nums1:
            if n not in nums2 and n not in numies1:
                numies1.append(n)
        for n in nums2:
            if n not in nums1 and n not in numies2:
                numies2.append(n)
        return [numies1, numies2]