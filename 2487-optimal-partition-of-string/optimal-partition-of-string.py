class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        partition = set()

        for char in s:
            if char in partition:
                partition = set()
                count += 1
            partition.add(char)
        return count