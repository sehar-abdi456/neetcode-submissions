class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #map each course to pre requisite list 
        #syntax: 
        preMap={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            preMap[crs].append(pre)
        #visit set along current path 
        visited=set()
        def dfs(crs):
            if crs in visited:
                return False 
            if preMap[crs]==[]:
                return True
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            preMap[crs]=[]
            return True
        for courses in range(numCourses):
            if not dfs(courses): return False
        return True 



        