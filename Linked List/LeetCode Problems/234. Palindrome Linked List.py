from typing import Optional
from collections import deque
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        stack = deque()
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        cur = head
        while cur:
            item = stack.pop()
            if item != cur.val:
                return False
            cur = cur.next
        return True