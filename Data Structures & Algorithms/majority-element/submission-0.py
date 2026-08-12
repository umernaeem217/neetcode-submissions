from collections import Counter
import heapq
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = Counter(nums)
        heap = []
        for key,value in counter.items():
            heapq.heappush(heap, (-value, key))
        
        value, key = heapq.heappop(heap)
        return key
