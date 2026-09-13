class Solution:
    def inrange(self, letter):
        num = ord(letter)
        if (num >= 65 and num <= 90):
            return True
        elif (num >= 97 and num <= 122):
            return True
        elif (num >= 48 and num <= 57):
            return True
        else:
            return False

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        s = s.lower()
        while left < right:
            while not self.inrange(s[left]) and left < right:
                left += 1
            while not self.inrange(s[right]) and left < right:
                right -= 1
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
        