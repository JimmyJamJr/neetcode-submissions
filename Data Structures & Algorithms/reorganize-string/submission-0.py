from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        if max(counts.values()) > (len(s) + 1) // 2:
            return ""

        heap = [(-c, ch) for ch, c in counts.items()]
        heapq.heapify(heap)
        res = []
        prev = None

        while heap:
            count, letter = heapq.heappop(heap) 
            res.append(letter)
            if prev:
                heapq.heappush(heap, prev)
            count += 1
            prev = (count, letter) if count < 0 else None
        return "".join(res)
        
