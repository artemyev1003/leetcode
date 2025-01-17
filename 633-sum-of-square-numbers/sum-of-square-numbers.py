class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = int(c ** 0.5)

        while a <= b:
            total = pow(a, 2) + pow(b, 2)
            if total > c:
                b -= 1
            elif total < c:
                a += 1
            else:
                return True
        return False