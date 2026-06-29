class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        mArea=0
        stack=[]
        #pair of index and height 
        for i,h in enumerate(heights):
            start=i
            while stack and stack[-1][1]>h:
                index,height=stack.pop()
                mArea=max(mArea,height*(i-index))
                start=index
            stack.append((start,h))
        for i,h in stack:
            mArea=max(mArea,h*(len(heights)-i))
        return mArea    

        