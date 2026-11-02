class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if root is None:
            return []
        delete_set = set(to_delete)
        output = [] if root.val in delete_set else [root]   # handle the original root up front

        stack = [root]
        while stack:
            node = stack.pop()
            deleted = node.val in delete_set

            for child in (node.left, node.right):
                if child is None:
                    continue
                stack.append(child)                          # visit every node, deleted or not
                if deleted and child.val not in delete_set:
                    output.append(child)                     # orphaned kept child starts a new tree

            # cut links to deleted children (parent's side)
            if node.left and node.left.val in delete_set:
                node.left = None
            if node.right and node.right.val in delete_set:
                node.right = None

        return output