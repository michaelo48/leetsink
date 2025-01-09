class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = 0
        m = len(height)-1
        maxVolume = 0
        volume = 0
        while n < m:
            diff = 0
            if height[n] > height[m]:
                diff = m - n
                volume = height[m] * diff
                m = m - 1
            
            else:
                diff = m - n
                volume = diff * height[n]
                n = n + 1
            if volume > maxVolume:
                maxVolume = volume
                

        return maxVolume

    

        