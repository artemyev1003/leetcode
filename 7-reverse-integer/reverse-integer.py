class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = abs(x)
        else:
            sign = 1

        ans = 0
        while x > 0:
            ans = ans * 10 + x % 10
            x = x // 10
        ans *= sign

        return ans if -2 ** 31 <= ans <= 2 ** 31 - 1 else 0