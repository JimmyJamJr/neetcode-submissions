class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i, c in enumerate(strs[0]):
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[j][i] != c:
                    return strs[0][:i]
        return strs[0]
