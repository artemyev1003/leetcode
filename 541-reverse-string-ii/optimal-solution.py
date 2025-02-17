class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(s), 2 * k):
            a[i:i+k] = list(reversed(a[i:i+k]))
        return "".join(a)

