# @param {Integer[]} nums
# @param {Integer} k
# @return {Integer}
def find_pairs(nums, k)
  nums_set = nums.to_set
  if k == 0
    freq = Hash.new(0)
    nums.each {|n| freq[n] += 1}
    ans = 0
    freq.values.each do |f|
      if f > 1
        ans += 1
      end
    end
    return ans
  else
    nums_set_k = nums_set.map {|n| n + k}
    return (nums_set & nums_set_k).length
  end
end
