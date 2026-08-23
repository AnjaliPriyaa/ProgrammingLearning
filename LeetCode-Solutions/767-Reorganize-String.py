class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = {}
        max_heap = []
        for i in s:
            freq[i] = freq.get(i,0)+1
        sorted_freq = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)
        if freq[sorted_freq[0]] > (len(s) + 1) // 2:
            return ""
        
        res = [None] * len(s)
        
        i = 0
        for char in sorted_freq:
            for _ in range(freq[char]):
                if i >= len(s):
                    i = 1
                res[i] = char
                i += 2
                
        return "".join(res)
            
