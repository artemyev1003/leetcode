from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{",
        }

        for char in s:
            if char in ["(", "[", "{"]:
                stack.append(char)
            else:
                try:
                    if mapping[char] != stack.pop():
                        return False
                except IndexError:
                    return False

        if len(stack) == 0:
            return True
        return False
