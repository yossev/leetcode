# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.str = ""
        self.help(root)
        return self.str
    
    def help(self, root):
        if not root:
            return
        self.str += str(root.val) 
        if root.left or root.right:
            self.str += "("
            self.help(root.left)
            self.str += ")"
        if root.right:
            self.str += "("
            self.help(root.right)
            self.str += ")"

        return self.str