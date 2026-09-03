# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        nodes = []
        dq = deque()
        dq.append(root)

        while dq:
            n = dq.popleft()
            if n:
                nodes.append(str(n.val))
            else:
                nodes.append("NULL")
            if n:
                dq.append(n.left)
                dq.append(n.right)
        return "_".join(nodes)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        nodes = data.split("_")

        if nodes[0] == "NULL":
            return None
            
        root = TreeNode(int(nodes[0]))
        dq = deque()
        dq.append(root)

        i = 1
        while dq:
            n = dq.popleft()

            left = nodes[i]
            right = nodes[i+1]
            i += 2

            if left != "NULL":
                n.left = TreeNode(int(left))
                dq.append(n.left)
            if right != "NULL":
                n.right = TreeNode(int(right))
                dq.append(n.right)
        return root



