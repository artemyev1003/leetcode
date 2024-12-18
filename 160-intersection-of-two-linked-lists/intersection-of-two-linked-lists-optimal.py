# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, head_a: ListNode, head_b: ListNode) -> ListNode | None:

        a = head_a
        b = head_b

        while a != b:
            a = a.next if a is not None else head_b
            b = b.next if b is not None else head_a

        return a
