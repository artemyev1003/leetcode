# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, head_a: ListNode, head_b: ListNode) -> ListNode | None:

        a = head_a
        b = head_b
        count_a = count_b = 0

        while a is not None:
            a = a.next
            count_a += 1

        while b is not None:
            b = b.next
            count_b += 1

        a = head_a
        b = head_b

        if count_a >= count_b:
            diff = count_a - count_b
            for _ in range(diff):
                a = a.next
        else:
            diff = count_b - count_a
            for _ in range(diff):
                b = b.next

        while a is not None or b is not None:
            if a == b:
                return a
            a = a.next
            b = b.next
        return None   