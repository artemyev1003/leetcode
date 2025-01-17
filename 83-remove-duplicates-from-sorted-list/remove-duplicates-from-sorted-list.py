class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head is None:
            return None
        
        curr_node = head
        next_node = head.next
        visited = {curr_node.val}

        while next_node is not None:
            if next_node.val in visited:
                curr_node.next = next_node.next
                next_node = next_node.next
            else:
                curr_node = next_node
                next_node = curr_node.next
                visited.add(curr_node.val)
        return head