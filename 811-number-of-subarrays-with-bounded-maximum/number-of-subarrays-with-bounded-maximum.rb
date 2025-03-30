def num_subarray_bounded_max(nums, left, right)
  def count(bound, nums)
    ans = count = 0
    for n in nums do
      count = n <= bound ? count + 1 : 0
      ans += count
    end
  return ans
  end
  return count(right, nums) - count(left - 1, nums)
end
