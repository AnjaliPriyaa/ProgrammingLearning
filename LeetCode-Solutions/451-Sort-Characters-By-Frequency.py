class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        new = ""
        for i in s:
            freq[i] = freq.get(i,0)+1
        for key,value in sorted(freq.items(), key=lambda x: x[1], reverse=True):
            new+=key*value
        return new

