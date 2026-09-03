# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def swapChildren(self, node):
        if not node:
            return
        self.swapChildren(node.left)
        self.swapChildren(node.right)
        node.left, node.right = node.right, node.left
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.swapChildren(root)
        return root
            
