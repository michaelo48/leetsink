class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        count = 0
        min = 0
        if a > b:
            min = b
        else:
            min = a
        for x in range(1, min+1):
            if a%x == 0 and b%x == 0:
                count += 1
        return count
