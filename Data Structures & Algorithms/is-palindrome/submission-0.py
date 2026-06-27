class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = "".join(char for char in s.lower() if char.isalnum())
        s_rev = ''.join(reversed(filtered_s))

        return filtered_s == s_rev