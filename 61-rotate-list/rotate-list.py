class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if head is None:
            return None
            
        slow, fast = head, head
        count = 1
        while fast.next is not None:
            fast = fast.next
            count += 1

        l = k % count
        for _ in range(count - l - 1):
            slow = slow.next

        if slow == fast:
            return head
        res = slow.next
        slow.next = None
        fast.next = head

        return res
