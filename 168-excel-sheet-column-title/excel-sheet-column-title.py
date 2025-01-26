class Solution:
    def convertToTitle(self, num: int) -> str:
        map = {}
        ans = ""
        for i, letter in enumerate(string.ascii_uppercase, start=1):
            map[i] = letter

        while num > 0:
            rem = num % 26
            num //= 26

            if rem == 0:
                rem += 26
                num -= 1
            ans = map[rem] + ans
        return ans