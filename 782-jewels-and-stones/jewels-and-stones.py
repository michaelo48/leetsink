class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        len1 = len(jewels)
        len2 = len(stones)
        for x in range(len1):
            for y in range(len2):
                if jewels[x] == stones[y]:
                    count += 1
        return count

