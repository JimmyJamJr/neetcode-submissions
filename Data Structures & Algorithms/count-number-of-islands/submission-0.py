class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        rows, cols = len(grid), len(grid[0])

        def dfs_destroy(r, c):
            if r < 0 or r >= rows:
                return
            if c < 0 or c >= cols:
                return
            if grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            dfs_destroy(r - 1, c)
            dfs_destroy(r + 1, c)
            dfs_destroy(r, c - 1)
            dfs_destroy(r, c + 1)
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs_destroy(r, c)
        
        return islands
            