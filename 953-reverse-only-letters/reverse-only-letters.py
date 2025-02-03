class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
       l = 0
       r = len(s) - 1
       res = list(s)

       while l < r:
           while not s[l].isalpha() and l < r:
               l += 1

           while not s[r].isalpha() and r > l:
                r -= 1

           res[l], res[r] = res[r], res[l]
           l += 1
           r -= 1
       return "".join(res) 
