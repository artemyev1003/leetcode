# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()
        tail = dummy_head
        while list1 is not None or list2 is not None:
            tail.next = ListNode()
            tail = tail.next
            if list1 is None:
                tail.val = list2.val
                list2 = list2.next
            elif list2 is None:
                tail.val = list1.val
                list1 = list1.next
            elif list1.val > list2.val:
                tail.val = list2.val
                list2 = list2.next
            else:
                tail.val = list1.val
                list1 = list1.next

        return dummy_head.next
        