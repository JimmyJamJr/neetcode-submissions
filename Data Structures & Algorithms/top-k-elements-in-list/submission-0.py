import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for n, freq in counts.items():
            buckets[freq].append(n)

        out = []
        for bucket in reversed(buckets):
            for n in bucket:
                out.append(n)
                if len(out) == k:
                    return out
