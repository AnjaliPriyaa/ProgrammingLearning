class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = range(0,len(nums)+1)
        a=set(nums)
        for i in res:
            if i not in a:
                return i
        