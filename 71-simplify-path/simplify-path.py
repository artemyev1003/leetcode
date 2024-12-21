from collections import deque


class Solution:
    def simplifyPath(self, path: str) -> str:
        result = deque()
        path += "/"
        word = ""
        for char in path:
            if char == "/" and word:
                if word == ".":
                    pass
                elif word == "..":
                    if result:
                        result.pop()
                else:
                    result.append(word)
                word = ""
            elif char == "/" and not word:
                pass
            else:
                word += char
        return "/" + "/".join(list(result))