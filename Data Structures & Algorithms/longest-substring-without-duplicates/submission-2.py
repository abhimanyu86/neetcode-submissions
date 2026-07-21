class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        for r in range(len(s)):
            while s[r] in s[l:r]:
                l += 1
            length = r - l + 1
            longest = max(length, longest)
        return longest