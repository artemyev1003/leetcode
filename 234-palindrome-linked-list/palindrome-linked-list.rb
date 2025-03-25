def is_palindrome(head)
  slow, fast = head, head
  while fast && fast.next
    slow = slow.next
    fast = fast.next.next
  end

  prev = slow
  slow = slow.next
  prev.next = nil

  while slow
      temp = slow.next
      slow.next = prev
      prev = slow
      slow = temp
  end

  fast = head
  slow = prev 

  while slow
      if slow.val != fast.val
        return false
      end
      slow = slow.next
      fast = fast.next
  end
  return true
end
