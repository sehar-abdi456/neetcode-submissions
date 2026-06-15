class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1=''
        for c in s:
            if c.isalnum():
                str1+=c.lower()
        return str1==str1[::-1]        
        