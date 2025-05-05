def rotate(nums, k)
k %= nums.length
nums[0...k], nums[k..-1] = nums[-k..-1], nums[0...nums.length - k]
end
