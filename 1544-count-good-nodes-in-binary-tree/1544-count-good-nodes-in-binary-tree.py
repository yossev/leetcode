# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def solve(node, max_val):
            if not node:
                return 0
            count=0
            if node.val >= max_val:
                count = 1
                max_val = node.val
            count += solve(node.right, max_val)
            count += solve(node.left, max_val)
            return count
        if not root:
            return 0
        return solve(root, root.val)