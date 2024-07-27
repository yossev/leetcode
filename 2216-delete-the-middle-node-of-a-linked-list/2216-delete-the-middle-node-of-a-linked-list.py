# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        # Hare turt


        # No head or only 1 node
        if not head or not head.next:
            return None
        
        turt=head
        hare=head
        before_turt = None

        while hare and hare.next:
            before_turt=turt
            turt=turt.next
            hare=hare.next.next

        if before_turt:
            before_turt.next=turt.next


        return head

        