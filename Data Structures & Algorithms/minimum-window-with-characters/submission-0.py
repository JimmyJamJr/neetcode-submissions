from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Build the freq we need
        need = Counter(t)
        
        freq = {}
        have = 0

        l, r = 0, 0
        best = float('inf')
        best_start = 0

        while r < len(s):
            freq[s[r]] = freq.get(s[r], 0) + 1
            if s[r] in need and freq[s[r]] == need[s[r]]:
                have += 1
            
            while have == len(need):
                if r - l + 1 < best:
                    best = r - l + 1
                    best_start = l

                freq[s[l]] = freq.get(s[l], 0) - 1
                if s[l] in need and freq[s[l]] < need[s[l]]:
                    have -= 1
                l += 1
            r += 1
        
        return s[best_start:best_start + best] if best < float('inf') else ""

            


