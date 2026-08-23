class Solution:
    def countSubstrings(self, s: str) -> int:
        result = []
        for i in range(len(s)): 
            for j in range(i,len(s)):
                slicing = s[i:j+1]
                if slicing == slicing[::-1]:
                    result.append(s[i:j+1])
        return len(result)
