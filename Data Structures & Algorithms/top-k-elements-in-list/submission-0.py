class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #push everything into maxheap and pop out first k
        count=Counter(nums)
        min_heap=[]
        #initialising minheap
        for num,freq in count.items():
            heapq.heappush(min_heap, (freq, num))
            if(len(min_heap)>k):
                heapq.heappop(min_heap)
        result = [item[1] for item in min_heap]

        return result
