from collections import deque
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first, second = list1, list2
        merged = tmp = ListNode(0)

        while first and second:
            if first.val < second.val:
                node = ListNode(first.val)
                merged.next = node
                first = first.next

            else:
                node = ListNode(second.val)
                merged.next = node
                second = second.next

            merged = merged.next

        if first:
            merged.next = first
        if second:
            merged.next = second

        return tmp.next
