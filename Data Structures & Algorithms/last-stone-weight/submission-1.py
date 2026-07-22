import heapq
class Solution:
    def lastStoneWeight(self, stones):
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while stones:
            if len(stones) <= 1:
                break
            w1 = heapq.heappop(stones)
            w2 = heapq.heappop(stones)
            if w1 == w2:
                continue
            res = abs(-w1-(-w2))
            if res != 0:
                heapq.heappush(stones, -res)
        return 0 if len(stones) == 0 else -stones[-1]
    