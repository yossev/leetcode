# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return

        deq = deque()
        curr = head
        while curr:
            deq.append(curr)
            curr = curr.next

        dummy = ListNode()
        curr = dummy

        while deq:
            if deq:
                curr.next = deq.popleft()
                curr = curr.next
            if deq:
                curr.next = deq.pop()
                curr = curr.next

        curr.next = None
        head = dummy.next

        