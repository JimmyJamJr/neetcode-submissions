# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = float("-inf")

        def maxAtNode(node):
            nonlocal best

            if not node:
                return 0
            
            left = maxAtNode(node.left)
            right = maxAtNode(node.right)

            node_best = max(
                left + node.val + right, 
                node.val + right,
                node.val + left,
                node.val
            )
            best = max(node_best, best)

            return max(node.val + right, node.val + left, node.val)
        
        maxAtNode(root)
        return best