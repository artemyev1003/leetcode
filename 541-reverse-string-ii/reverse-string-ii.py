class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        list_s = list(s)
        for i in range(len(list_s)):
            if (i + 1) % (2 * k) == 0:
                r = i - k
                l = r - k + 1
                self._reverse(list_s, l, r)
        if (rem := len(list_s) % (2 * k)) > 0:            
            if rem < k:
                l = i - rem + 1
                r = i
                self._reverse(list_s, l, r)
            else:
                l = i - rem + 1 
                r = l + k - 1
                self._reverse(list_s, l, r)
        return "".join(list_s)
    
    def _reverse(self, arr: list[int], l: int, r: int) -> None:
        while l < r:
            arr[l],arr[r] =arr[r],arr[l]
            l += 1
            r -= 1
