class Solution:
    def reverseWords(self, s: str) -> str:
        word = ""
        a = []
        for char in s:
            if char != " ":
                word = char + word
            else:
                if word:
                    a.append(word)
                    word = ""
        if word:
            a.append(word)
        return " ".join(a)
