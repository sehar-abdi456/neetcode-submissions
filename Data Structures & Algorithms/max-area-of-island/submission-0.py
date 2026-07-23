class Solution:
    def dfs(self,grid,i,j)->int:
        maxi=0
        grid[i][j]=0
        maxi+=1
        moves=[(-1,0),(0,-1),(0,1),(1,0)]
        for dx,dy in moves:
            nx,ny=i+dx,j+dy
            if 0<=nx<len(grid) and 0<=ny<len(grid[0]) and grid[nx][ny]==1:
                maxi += self.dfs(grid, nx, ny)
        return maxi

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        #perform dfs for every component and store size of current result 
        if not grid:
            return 0
        n=len(grid)
        m=len(grid[0])
        
        maxim=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    max1=self.dfs(grid,i,j)
                    maxim=max(maxim,max1)
        return maxim

                    


                
        



        