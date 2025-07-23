# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        firstBad, start, end = 0, 1, n
        while start <= end:
            middle = (start + end)//2
            if isBadVersion(middle):
                firstBad = middle
                end = middle - 1
            else:
                start = middle + 1
        return firstBad
        
        

        