class Solution(object):
    def addTwoNumbers(self, l1, l2):
        num1 = 0
        num2 = 0

        temp1, temp2 = l1, l2

        place = 1
        while temp1:
            num1 += temp1.val * place
            place *= 10
            temp1 = temp1.next

        place = 1
        while temp2:
            num2 += temp2.val * place
            place *= 10
            temp2 = temp2.next

        _sum = num1 + num2

        dummy = ListNode(-1)
        curr = dummy

        for digit in reversed(str(_sum)):
            curr.next = ListNode(int(digit))
            curr = curr.next

        return dummy.next
