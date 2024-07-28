# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def solve(node, val):
            if node is None:
                return None
            if node.val == val:
                return node
            if node.val > val:
                return solve(node.left, val)
            return solve(node.right, val)
        
        return solve(root, val)
