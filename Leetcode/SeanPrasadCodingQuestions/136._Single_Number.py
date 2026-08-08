class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        singleno = {}
        for i in nums:
            if i not in singleno:
                singleno[i] = 0
            singleno[i]+=1
        for i in singleno:
            if singleno[i]==1:
                return i
        return -1
