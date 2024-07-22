# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        turtoise = head
        rabbit = head

        while rabbit!=None and rabbit.next!=None:
            turtoise=turtoise.next
            rabbit = rabbit.next.next

            if rabbit == turtoise:
                return True
        return False
        