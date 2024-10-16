class Solution:
    def isHappy(self, n: int) -> bool:
        results = set()
        while True:
            if n == 1:
                return True
            s = 0
            for char in str(n):
                s += int(char) ** 2
            n = s
            if s in results:
                return False
            results.add(s)