# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        result = []

        while list1:
            result.append(list1.val)
            list1 = list1.next

        while list2:
            result.append(list2.val)
            list2 = list2.next

        result.sort()

        dummy = ListNode()
        current = dummy

        for value in result:
            current.next = ListNode(value)
            current = current.next

        # Return the node after the dummy node
        return dummy.next
