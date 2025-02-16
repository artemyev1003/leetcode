class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        list_s = list(s)
        for i in range(len(list_s)):
            if (i + 1) % (2 * k) == 0:
                r = i - k
                l = r - k + 1
                print("l = ", l)
                print("r = ", r)
                self._reverse(list_s, l, r)
                print("list_s = ", list_s)
        if (rem := len(list_s) % (2 * k)) > 0:
            
            print("rem = ", rem)
            if rem < k:
                print("wo")
                l = i - rem + 1
                r = i
                print("l = ", l)
                print("r = ", r)
                self._reverse(list_s, l, r)
                print("list_s = ", list_s)
            else:
                print("here")
                l = i - rem + 1 
                r = l + k - 1
                print("l = ", l)
                print("r = ", r)
                self._reverse(list_s, l, r)
                print("list_s = ", list_s)
        return "".join(list_s)
    
    def _reverse(self, arr: list[int], l: int, r: int) -> None:
        while l < r:
            arr[l],arr[r] =arr[r],arr[l]
            l += 1
            r -= 1
