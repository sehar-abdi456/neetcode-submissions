class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        l,r=0,len(height)-1
        leftmax,rightmax=height[l],height[r]
        res=0
        while l<r:
            #already applying this condition so theres no need to check manually again
            #its given that value at left is less that right so we have our minimum 
            if leftmax<=rightmax:
                res+=leftmax-height[l]
                l+=1
                #attempting to shift minimum height 
                #basically want max of left and right and then find min of left and right 
                leftmax=max(leftmax,height[l])
               
            else:
                res+=rightmax-height[r]
                r-=1
                rightmax=max(rightmax,height[r])
                
        return res    

               



        