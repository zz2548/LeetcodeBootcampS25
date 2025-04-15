# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q:
            return root
        leftTarget = rightTarget = None
        if root.left is not None:
            leftTarget = self.lowestCommonAncestor(root.left, p, q)
        if root.right is not None:
            rightTarget = self.lowestCommonAncestor(root.right, p, q)
        if leftTarget and rightTarget: # parent is the LCA
            return root
        else: # One of the results is LCA
            return leftTarget or rightTarget