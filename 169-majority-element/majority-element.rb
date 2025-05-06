def majority_element(nums)
  n = nums.length / 2 
  nums.sort!
  curr = nums[0]
  count = 0
  nums.each do |num|
    if num == curr
      count += 1
      if count > n
        return num
      end
    else
      count = 1
      curr = num
    end
  end
end
