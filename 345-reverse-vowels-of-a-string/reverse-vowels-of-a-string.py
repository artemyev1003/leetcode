class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = "aeiouAEIOU"
        l = 0
        r = len(s) - 1
        ans = list(s)

        while l < r:
            if ans[l] not in vowels:
                l += 1
                continue

            if ans[r] not in vowels:
                r -= 1
                continue
            
            ans[l], ans[r] = ans[r], ans[l]
            l += 1
            r -= 1
        return "".join(ans)
