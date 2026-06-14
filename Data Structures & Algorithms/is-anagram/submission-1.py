class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        num1=len(s)
        num2=len(t)
        if num1!=num2:return False
        set1=Counter(s)
        set2=Counter(t)
        if(set1==set2): 
            return True 
        else: 
            return False        
        