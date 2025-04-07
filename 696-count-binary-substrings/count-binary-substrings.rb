# @param {String} s
# @return {Integer}
def count_binary_substrings(s)
  fast = slow = count_1 = count_2 = ans = 0
  l = s.length
  while fast < l
    while s[fast] == s[slow] and fast < l
      count_1 += 1
      fast += 1
    end
    slow = fast - 1
    while s[fast] != s[slow] and fast < l
      count_2 += 1
      fast += 1
    end
    slow += 1
    ans += [count_1, count_2].min
    count_1 = count_2
    count_2 = 0
  end
  return ans
end
