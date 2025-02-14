class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        l = 0
        _max = len(arr)
        r = _max - 1
        ans = []

        while l < r:
            if arr[r] != _max:
                while arr[l] != _max:
                    l += 1
                ans.append(l + 1)
                ans.append(r + 1)
                self._flip(arr, 0, l)
                self._flip(arr, 0, r)
            r -= 1
            _max -= 1
            l = 0
            print(arr)
        return ans

    def _flip(self, arr: list[int], l: int, r: int) -> list[int]:
        while l <= r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
        return arr

