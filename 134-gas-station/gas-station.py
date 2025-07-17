class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        start = 0
        difference = 0
        for x in range(len(gas)):
            difference += (gas[x] - cost[x])

            if difference < 0:
                difference = 0
                start = x + 1
        return start
        