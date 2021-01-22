### Binary Tree Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        level = []
        if hasattr(root, 'val'):
            if root.val is not None:
                self.traverse(root, level)
        return level

    def traverse(self, node, level=[]):
        appended = False
        if hasattr(node, 'left'):
            if node.left:
                self.traverse(node.left, level)
                level.append(node.val)
                appended = True

        if hasattr(node, 'right'):
            if node.right:
                if not appended:
                    level.append(node.val)
                    appended = True
                self.traverse(node.right, level)
        if not appended:
            level.append(node.val)