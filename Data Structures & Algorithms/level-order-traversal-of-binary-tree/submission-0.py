# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        output = []
        dq = deque()
        dq.append((root, 0))

        while dq:
            n, level = dq.popleft()
            if level >= len(output):
                output.append([])
            output[level].append(n.val)
            if n.left:
                dq.append((n.left, level + 1))
            if n.right:
                dq.append((n.right, level + 1))

        return output
