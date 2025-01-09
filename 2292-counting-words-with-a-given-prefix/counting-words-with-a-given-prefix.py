class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        count = 0
        max_pref_idx = len(pref)
        for word in words:
            if len(word) < max_pref_idx:
                continue
            for i in range(max_pref_idx):
                if pref[i] != word[i]:
                    break
            else:
                count += 1
        return count