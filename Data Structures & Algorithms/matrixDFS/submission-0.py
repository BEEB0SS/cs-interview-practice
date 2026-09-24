class Solution:
    def countPathsHelper(self, grid, r, c, visit):
        ROWS = len(grid)
        COLS = len(grid[0])
        if r < 0 or c < 0 or r == ROWS or c == COLS or (r, c) in visit or grid[r][c] == 1:
            return 0
        if r == ROWS - 1 and c == COLS - 1:
            return 1
        
        visit.add((r,c))
        count = 0
        count += self.countPathsHelper(grid, r + 1, c, visit)
        count += self.countPathsHelper(grid, r - 1, c, visit)
        count += self.countPathsHelper(grid, r, c + 1, visit)
        count += self.countPathsHelper(grid, r, c - 1, visit)
        visit.remove((r,c))
        return count

    def countPaths(self, grid: List[List[int]]) -> int:
        return self.countPathsHelper(grid, 0, 0, set())

        