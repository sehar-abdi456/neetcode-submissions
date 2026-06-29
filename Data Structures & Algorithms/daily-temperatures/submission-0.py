class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res= [0]*len(temperatures)
        stack=[] #pair [temp,index]
        for i,t in enumerate(temperatures):
            while stack and t>stack[-1][0]:
                topTemp,topInd=stack.pop()
                res[topInd]=(i-topInd)
            stack.append([t,i])
        return res    


                
            #stack[-1] is the topmost element in a stack(python syntax)

        
        