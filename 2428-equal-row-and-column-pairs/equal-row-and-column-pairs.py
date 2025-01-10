class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        columns = []
        count = 0
        for h in range(len(grid)):
            column = []
            for n in grid:
                column.append(n[h])
            columns.append(column)

        for i in grid:
            for j in columns:
                if i == j:
                    count = count + 1
        return count
            


