from typing import Optional
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        slow = fast = head
        found = False

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                found = True
                break

        if not found:
            return None
        cur = head
        while cur is not slow:
            cur = cur.next
            slow = slow.next
        return cur