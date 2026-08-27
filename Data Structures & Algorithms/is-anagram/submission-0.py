class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = {}
        for c in s:
            if c in counts.keys():
                counts[c] += 1
            else:
                counts[c] = 1
        
        for c in t:
            if c not in counts.keys():
                return False
            if counts[c] == 0:
                return False
            counts[c] -= 1
            
        return True
