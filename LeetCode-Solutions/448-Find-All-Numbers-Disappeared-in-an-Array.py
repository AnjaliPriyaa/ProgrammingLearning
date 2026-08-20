class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        notlist = []
        a = set(nums)
        res = range(1,len(nums)+1)
        for i in res:
            if i not in a:
                notlist.append(i)
        return notlist
