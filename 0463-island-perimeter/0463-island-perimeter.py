class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])

        perimeter = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    perimeter += 4

                    # Check right
                    if c + 1 < cols and grid[r][c + 1] == 1:
                        perimeter -= 2

                    # Check down
                    if r + 1 < rows and grid[r + 1][c] == 1:
                        perimeter -= 2

        return perimeter
        