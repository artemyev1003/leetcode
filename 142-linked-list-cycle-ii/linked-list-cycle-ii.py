class Solution:
    def detectCycle(self, head: ListNode | None) -> ListNode | None:
        fast = slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next 
            fast = fast.next.next
            
            if fast == slow:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None  
