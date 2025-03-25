def find_duplicate(nums)
  slow, fast = 0, 0
  while true
    slow = nums[slow]
    fast = nums[nums[fast]]
    if slow == fast
      break
    end
  end 

  fast = 0
  while true
    slow = nums[slow]
    fast = nums[fast]
    if slow == fast
      return slow
    end
  end
end
