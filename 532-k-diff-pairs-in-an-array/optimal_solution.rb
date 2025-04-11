def find_pairs(nums, k)
  pairs = Set.new
  visited = Set.new
  nums.each do |num|
    pairs.add([num - k, num]) if visited.include?(num - k)
    pairs.add([num, num + k]) if visited.include?(num + k)
    visited.add(num)
  end
  pairs.length
end
