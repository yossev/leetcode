# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, res):
            if not node:
                return 0
            
            left = helper(node.left, res)
            right =  helper(node.right, res)

            res[0] = max(res[0], left+right)

            return max(left, right)+1
        res = [0]

        helper(root, res)

        return res[0]