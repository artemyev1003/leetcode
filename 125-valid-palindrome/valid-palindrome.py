import string


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.strip().lower()
        alphanumeric = string.ascii_lowercase + string.digits
        p1 = 0
        p2 = len(s) - 1

        while p1 <= p2:
            if s[p1] not in alphanumeric:
                p1 += 1
                continue
            if s[p2] not in alphanumeric:
                p2 -= 1
                continue

            if s[p1] == s[p2]:
                p1 += 1
                p2 -= 1
            else:
                return False
        return True