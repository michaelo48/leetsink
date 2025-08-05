class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sum = 0
        temp = x
        while x > 0:

            sum += x % 10
            x //= 10



        if temp%sum == 0:
            return sum
        else:
            return -1
    


