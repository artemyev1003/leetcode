class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        l = ans = 0
        r = len(people) - 1

        while l < r:
            if people[l] + people[r] <= limit:
                l += 1
                r -= 1
            else:
                r -= 1
            ans += 1
        if l == r:
            ans += 1
        return ans