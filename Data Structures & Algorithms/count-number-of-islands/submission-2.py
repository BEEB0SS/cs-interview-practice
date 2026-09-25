class Solution:
    def numIslandsHelper(self, grid, r, c, visit):
        ROWS = len(grid)
        COLS = len(grid[0])
        if r < 0 or c < 0 or r == ROWS or c == COLS or (r,c) in visit:
            return count, visit
        #mark the island as visited
        visit.add((r,c))
        if int(grid[r][c]) == 1:
            self.numIslandsHelper(grid, r+1, c, visit)
            self.numIslandsHelper(grid, r-1, c, visit)
            self.numIslandsHelper(grid, r, c+1, visit)
            self.numIslandsHelper(grid, r, c-1, visit)
        return visit


    
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        island_counter = 0
        r, c = 0, 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if (r, c) in visit or int(grid[r][c]) == 0:
                    continue
                else:
                    visit = self.numIslandsHelper(grid, r, c, visit)
                    island_counter += 1
        return island_counter

        