class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        row_len = len(image[0]) - 1
        for row in image:
            l = 0
            r = row_len
            while l <= r:
                row[l], row[r] = ~row[r] & 1, ~row[l] & 1
                l += 1
                r -= 1
        return image
