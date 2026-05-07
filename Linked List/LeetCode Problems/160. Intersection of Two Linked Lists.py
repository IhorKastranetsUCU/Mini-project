from collections import deque
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s_A = deque()
        s_B = deque()

        cur_A = headA
        cur_B = headB

        while cur_A:
            s_A.append(cur_A)
            cur_A = cur_A.next

        while cur_B:
            s_B.append(cur_B)
            cur_B = cur_B.next

        ans = None
        while s_A and s_B:
            a = s_A.pop()
            b = s_B.pop()
            if a is b:
                ans = a
            else:
                break
        return ans