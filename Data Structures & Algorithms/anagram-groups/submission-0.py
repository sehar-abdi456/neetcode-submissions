class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ref1= defaultdict(list)
        #attempt to map char count to list in python
        for s in strs:
            count= [0]*26
            for c in s:
                count[ord(c)-ord("a")]+=1
                #to map to asci 
            ref1[tuple(count)].append(s)   
            #same count append 
            #dictionary keys should be immutable-tuple
        return list(ref1.values())   
        #old python versions used to return a list to ref1.values() now it returns a view object 
        #typecaste




        