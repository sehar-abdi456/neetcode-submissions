class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue;
                #that means triplet has already been searched for that element 
            l,r=i+1,len(nums)-1
            while l<r:
                threeS=a+nums[l]+nums[r]
                if threeS>0:
                    r-=1
                elif threeS<0:
                    l+=1
                else:
                    res.append([a,nums[l],nums[r]])
                    l+=1
                    #move onto next 
                    while nums[l]==nums[l-1] and l<r:
                        l+=1          
        return res
        