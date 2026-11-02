class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        last_seen = {}
        longest = 0
        repeat_count = 0
        for right,letter in enumerate(s):
            if letter in last_seen and last_seen[letter] >= left:
                left = last_seen[letter]+1

            last_seen[letter] = right
            if right-left>=longest:
                longest = (right-left)+1
        return longest
        