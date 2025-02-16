class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for r in range(len(word)):
            if word[r] == ch:
                l = 0
                word_list = list(word) 
                while l <= r:
                    word_list[l], word_list[r] = word_list[r], word_list[l]
                    l += 1
                    r -= 1
                return "".join(word_list) 
            else:
               r += 1
        return word
