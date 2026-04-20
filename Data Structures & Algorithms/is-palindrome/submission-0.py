class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(ch for ch in s if ch.isalnum()).upper()
        return s==s[::-1]
        