class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair= [[p,s] for p,s in zip(position,speed)]
        # array of position and speed together 
        stack=[]
        for p,s in sorted(pair)[::-1]:
            stack.append((target-p)/s)
            # if cars reach destination at the same time, they're part of one fleet
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()
        return len(stack)        


        