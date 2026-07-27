class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #define parent #define rank 
        parent= [i for i in range(n)]
        rank=[1]*n

        def find(n1):
            #for node n1 find root parent 
            res=n1
            while res!=parent[res]:
                res=parent[res]
                #keep going up the chain 
            return res 
        def union(n1,n2):
            #union of these two
            p1,p2=find(n1),find(n2)
            if p1==p2:
                return 0
            #here we do union by rank 
            if rank[p2]>rank[p1]:
                parent[p1]=p2
                rank[p2]+=rank[p1]
            else:
                parent[p2]=p1
                rank[p1]+=rank[p2]
            return 1
        res=n
        for n1,n2 in edges:
            res-=union(n1,n2)
        return res 


        