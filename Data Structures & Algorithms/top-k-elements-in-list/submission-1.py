from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        heap = []
        for key, value in counter.items():
            heapq.heappush(heap, (-value, key))
        res = []
        for _ in range(k):
            val, key = heapq.heappop(heap)
            res.append(key)
        return res