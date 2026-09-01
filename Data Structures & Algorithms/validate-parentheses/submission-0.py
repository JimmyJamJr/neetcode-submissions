class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for c in s:
            if c in mapping.values():
                stack.append(c)
            else:
                if len(stack) == 0 or stack[-1] != mapping[c]:
                    return False
                stack.pop()
        return len(stack) == 0