class Solution:
    def dfs(self,grid,i,j):
        grid[i][j]="0"
        moves=[(-1,0),(0,-1),(1,0),(0,1)]
        for dx,dy in moves:
            nx,ny=i+dx,j+dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == "1":
                self.dfs(grid,nx,ny)
    def numIslands(self, grid: List[List[str]]) -> int:
        # number of disconnected elements 
        # dfs 
        if not grid:
            return 0
        n=len(grid)
        m=len(grid[0])
        islands=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    islands+=1
                    self.dfs(grid,i,j)
        return islands 

        