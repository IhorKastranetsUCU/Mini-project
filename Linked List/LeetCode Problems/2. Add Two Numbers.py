from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        tmp = ans
        reminder = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            node_val = val1 + val2 + reminder

            if node_val >= 10:
                reminder = 1
                node_val -= 10
            else:
                reminder = 0

            tmp.next = ListNode(node_val)
            tmp = tmp.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if reminder:
            tmp.next = ListNode(reminder)

        return ans.next

        ans = ListNode()
        tmp = ans
        reminder = 0
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            node_val = val1 + val2 + reminder

            if node_val >= 10:
                reminder = 1
                node_val -= 10
            else:
                reminder = 0

            tmp.next = ListNode(node_val)
            tmp = tmp.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if reminder:
            tmp.next = ListNode(reminder)

        return ans.next
