class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        else:
            for i in range(1, len(digits)):
                if digits[-i] == 9:
                    digits[-i] = 0
                else:
                    digits[-i] += 1
                    return digits

            if digits[0] == 9:
                digits[0] = 1
                digits.append(0)
            else:
                digits[0] += 1
                return digits
            return digits