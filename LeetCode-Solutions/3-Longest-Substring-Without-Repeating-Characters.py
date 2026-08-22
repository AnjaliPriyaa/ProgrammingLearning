class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # result = []
        max_len = 1
        if s == "":
            return 0
        for i in range(len(s)):
            substring = s[i]
            for j in range(i+1,len(s)):
                if s[j] not in substring:
                    substring+=s[j]
                    max_len = max(max_len,len(substring))
                else:
                    break
        #     if substring not in result:
        #         result.append(substring)
        # for i in result:
        #     if len(i) == max_len:
        #         print(i)
        return max_len



        