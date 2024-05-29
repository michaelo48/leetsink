class Solution(object):
    def isPowerOfFour(self, n):
        if(n<1):
            return False
        elif(n == 1):
            return True
        
        
        powerNum = 4
        count = 1

        while(powerNum <= n):
            if(powerNum == n):
                return True
            else:
                powerNum = math.pow(4, count)
                count += 1
        return False
        """
        :type n: int
        :rtype: bool
        """
        