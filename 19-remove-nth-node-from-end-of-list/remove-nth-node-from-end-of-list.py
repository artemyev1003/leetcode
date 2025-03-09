class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        slow, fast = head, head
        count = 0

        while count < n:
            fast = fast.next
            count += 1

        if fast is None:
            return slow.next

        while fast.next is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        
        return head
