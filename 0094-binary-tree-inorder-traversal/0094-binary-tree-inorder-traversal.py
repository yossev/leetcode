# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def helper(root, res):
            if not root: 
                return None
            
            helper(root.left, res)

            res.append(root.val)

            helper(root.right, res)

        res = []
        helper(root, res)
        return res