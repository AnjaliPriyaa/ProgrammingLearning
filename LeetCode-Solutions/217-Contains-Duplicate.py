class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = set(nums)
        # for i in nums:
        #     if i not in duplicate:
        #         duplicate.add(i)
        #     else:
        #         return True
        # return False
        return not len(duplicate)==len(nums)


        
        