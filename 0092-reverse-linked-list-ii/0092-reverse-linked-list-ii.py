# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        dummy = ListNode(0)
        dummy.next = head

        pLeft = dummy
        pos = 1

        while pos < left:
            pLeft = pLeft.next
            pos += 1


        curr = pLeft.next
        prev = None

        # Reverse the List
        for i in range(right - left + 1):
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt
        
        
        pLeft.next.next = curr   # tail connects to remainder
        pLeft.next = prev 
        

        return dummy.next