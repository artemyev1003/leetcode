class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        track = dict()
        length = len(s)
        fast = slow = 0
        ans = 0

        while fast < length:
            if s[fast] not in track:
                track[s[fast]] = fast
                fast += 1
            else:
                if (curr := len(track)) > ans:
                    ans = curr
                slow_pos = track[s[fast]] + 1
                while slow != slow_pos:
                    track.pop(s[slow])
                    slow += 1

            if (curr := len(track)) > ans:
                ans = curr
        return ans