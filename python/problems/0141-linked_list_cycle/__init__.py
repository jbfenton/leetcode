class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        current = head

        while current:
            if hasattr(current, 'found'):
                return True
            else:
                current.found = True
                current = current.next

        return False
