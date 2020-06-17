class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        current = head
        lookup = set()

        while current:
            if current in lookup:
                return True
            else:
                lookup.add(current)
                current = current.next

        return False
