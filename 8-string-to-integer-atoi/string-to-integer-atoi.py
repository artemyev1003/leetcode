class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        num_s = ""
        sign_flag = False
        max_val = 2 ** 31 - 1
        min_val = -2 ** 31

        if s and s[0] in "+-":
            num_s += s[0]
            sign_flag = True
            s = s[1:]

        for char in s:
            if char.isdigit():
                num_s += char
            else:
                break

        num = int(num_s) if not sign_flag and num_s or sign_flag and num_s[1:] else 0
        if num > max_val:
            num = max_val
        if num < min_val:
            num = min_val

        return num