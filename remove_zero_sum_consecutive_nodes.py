# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        while True:
            cur = head
            if cur.next is not None and cur.next.val + cur.val == 0:
                head = cur.next.next
                continue
            while cur.next.next is not None:
                if cur.next.val + cur.next.next.val == 0:
                    cur.next = cur.next.next.next
                    continue

        return head
