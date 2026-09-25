class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        max_length = 0
        chars = {}
        L = 0
        for i in range(len(s)):
            if s[i] not in chars:
                chars[s[i]] = i
            else:
                diff = i - L
                if diff > max_length:
                    max_length = diff
                if chars[s[i]] < L:
                    chars[s[i]] = i
                else:
                    L = chars[s[i]] + 1
                    chars[s[i]] = i
        if len(s) - L > max_length:
            max_length = len(s) - L
        return max_length


        

        