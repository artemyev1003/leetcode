class Solution:
    def validPalindrome(self, s: str) -> bool:
        count = l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                if self._is_palindrome(s[l+1:r+1]):
                    return True
                elif self._is_palindrome(s[l:r]):
                    return True
                return False
            else:
                l += 1
                r -= 1
        return True

    def _is_palindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
