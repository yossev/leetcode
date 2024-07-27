# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head is None:
            return None
        
        odd=head
        even=odd.next
        even_head = even

        while even and even.next:
            odd.next=even.next
            odd=even.next
            even.next = odd.next
            even = even.next
        odd.next=even_head

        return head