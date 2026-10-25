class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        min_so_far = min(self.stack[-1][1], val) if self.stack else val
        self.stack.append((val, min_so_far))

    def pop(self) -> None:
        val, _ = self.stack.pop()
        return val

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
