class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        if s == s[::-1]:
            return s
        for i in range(len(s)):
            for j in range(i,len(s)):
                substring = s[i:j+1]
                if substring == substring[::-1] and len(result)<len(substring):
                    result = substring
        return result

        