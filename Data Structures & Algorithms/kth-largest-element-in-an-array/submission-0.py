class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        maxHeap=[-num for num in nums ]
        heapq.heapify(maxHeap)
        for _ in range(k - 1):
            heapq.heappop(maxHeap)
        ans=heapq.heappop(maxHeap)
        return -ans
        