class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        p1, p2 = 0, 0
        index = 1

        while p1 <= len(haystack) - len(needle):
            if haystack[p1] == needle[0]:
                for p2 in range(p1+1, p1 + len(needle)):
                    if haystack[p2] != needle[index]:
                        index = 1
                        break
                    index += 1
                else:
                    return p1
            p1 += 1
        return -1
