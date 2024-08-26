"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution(object):

    def helper(self, current_node, res):
        if not current_node:
            return
        for child in current_node.children:
            self.helper(child, res)     
        res.append(current_node.val)
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        res=[]
        self.helper(root, res)
        return res
