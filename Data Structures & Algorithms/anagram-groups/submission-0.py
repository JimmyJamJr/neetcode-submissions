class Solution:
    def getCounts(self, s: str) -> List[int]:
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        return tuple(counts)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            counts = self.getCounts(s)
            if counts in groups:
                groups[counts].append(s)
            else:
                groups[counts] = [s]
        
        return list(groups.values())
