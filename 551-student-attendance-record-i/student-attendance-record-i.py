class Solution(object):
    def checkRecord(self, s):
        count = 0
        count1 = 0
        for x in s:
            if( x == "A"):
                count+=1
            if( x == "L"):
                count1+=1
            else:
                count1 = 0
            if(count == 2 or count1 == 3):
                return False
        return True

        """
        :type s: str
        :rtype: bool
        """
        