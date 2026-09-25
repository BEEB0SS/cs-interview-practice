from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topk = []
        result = []
        num_counts = Counter(nums)
        #print(num_counts)
        for num in num_counts:
            heapq.heappush(topk, (-(num_counts[num]), num))
        for i in range(k):
            freq, num = heapq.heappop(topk)
            result.append(num)
        return result
        
        