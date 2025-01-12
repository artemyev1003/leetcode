class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        letters = set(s)
        len_s = len(s)
        ans = 0

        for letter in letters:
            l = count = others_count = 0

            for r in range(len_s):
                if s[r] == letter:
                    count += 1
                else:
                    others_count += 1

                if others_count == k + 1:
                    ans = max(ans, count + k)
                    while others_count != k:
                        if s[l] == letter:
                            count -= 1
                        else:
                            others_count -= 1
                        l += 1
            ans = max(ans, count + others_count)
        return ans