# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        current = head
        carry = 0

        while l1 or l2:
            val_1 = 0
            val_2 = 0

            if l1:
                val_1 = l1.val
                l1 = l1.next

            if l2:
                val_2 = l2.val
                l2 = l2.next

            total = val_1 + val_2 + carry
            carry = total // 10
            total = total % 10

            current.next = ListNode(total)
            current = current.next

        if carry:
            current.next = ListNode(carry)

        return head.next
