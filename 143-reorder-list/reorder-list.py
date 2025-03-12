class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        if head is None or head.next is None or head.next.next is None:
            return

        fast = head
        while fast.next.next is not None:
            fast = fast.next

        last = fast.next
        last.next = head.next
        head.next = last
        fast.next = None

        self.reorderList(last.next)
