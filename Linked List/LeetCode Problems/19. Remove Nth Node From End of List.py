from typing import Optional
from collections import deque

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        q = deque()
        cur = head
        while cur:
            q.append(cur)
            cur = cur.next
        if n == len(q):
            return head.next
        prev = q[-n-1]
        prev.next = prev.next.next
        return head