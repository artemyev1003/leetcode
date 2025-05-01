def duplicate_zeros(arr)
  zeroes = arr.count(0)
  n = arr.length
  for i in (n - 1).downto(0)
    if i + zeroes < n
      arr[i + zeroes] = arr[i]
    end
    if arr[i] == 0
      zeroes -= 1
      if i + zeroes < n
        arr[i + zeroes] = 0
      end
    end
  end
end
