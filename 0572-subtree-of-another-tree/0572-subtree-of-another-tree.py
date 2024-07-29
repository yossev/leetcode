# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        def check(node, subRoot):
            if not node and not subRoot:
                return True
            if not node or not subRoot:
                return False
            if node.val != subRoot.val:
                return False
            return check(node.left, subRoot.left) and check(node.right, subRoot.right)

        if not root:
            return False
        if check(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
