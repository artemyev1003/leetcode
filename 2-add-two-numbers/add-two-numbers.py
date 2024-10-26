# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        head, counter = self.calculate_node(l1, l2, 0)
        curr_node = head

        l1 = self.get_next_node(l1)
        l2 = self.get_next_node(l2)

        while any([l1, l2]) or counter:
            next_node, counter = self.calculate_node(l1, l2, counter)
            curr_node.next = next_node
            curr_node = next_node
            
            l1 = self.get_next_node(l1)
            l2 = self.get_next_node(l2)

        return head

    @staticmethod
    def calculate_node(l1: ListNode | None, l2: ListNode | None, counter: int) -> tuple[ListNode, int]:
        node = ListNode()
        if (result_val := counter + (l1.val if l1 else 0) + (l2.val if l2 else 0)) > 9:
            node.val = result_val % 10
            counter = 1
        else:
            node.val = result_val
            counter = 0
        return node, counter

    @staticmethod
    def get_next_node(ln: ListNode | None) -> ListNode | None:
        return ln.next if ln else None