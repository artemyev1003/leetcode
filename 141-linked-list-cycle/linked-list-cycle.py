class Solution:
    def hasCycle(self, head: ListNode | None) -> bool:

        visited_nodes = [head]
        curr_node = head.next if head is not None else None

        while curr_node is not None:
            curr_node = curr_node.next
            if curr_node in visited_nodes:
                return True
            visited_nodes.append(curr_node)
        return False