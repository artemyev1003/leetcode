class Solution:
    def romanToInt(self, s: str) -> int:
        num_mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        result = 0
        length = len(s)
        for i in range(length):
            curr = num_mapping[s[i]]
            if i < length - 1 and curr < num_mapping[s[i + 1]]:
                result -= curr
            else:
                result += curr
        return result
