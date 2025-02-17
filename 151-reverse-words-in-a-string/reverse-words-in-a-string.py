from collections import deque

class Solution:
    def reverseWords(self, s: str) -> str:
        a = deque()
        word = ""

        for char in s:
            if char != " ":
                word += char
            else:
                if word:
                    a.appendleft(word)
                    word = ""
        if word:
            a.appendleft(word)
        return " ".join(a) 
