class Solution(object):
    def addDigits(self, num):
        while num >= 10:
            num = sum(int(x) for x in str(num))
        return num


        

        