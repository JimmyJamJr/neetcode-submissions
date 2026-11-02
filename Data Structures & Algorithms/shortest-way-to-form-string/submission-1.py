class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        t = 0
        count = 0

        while t < len(target):
            s = 0
            moved = False 
            count += 1
            while s < len(source) and t < len(target):
                if source[s] == target[t]:
                    t += 1
                    moved = True
                s += 1
            if not moved:
                return -1
        return count