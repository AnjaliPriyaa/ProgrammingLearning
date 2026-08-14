class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Brute Force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] == target:
        #             return [i,j]

        #Optimal Solution (enumerate(list) → index, value and dict.items() → key, value)
        pair ={}
        for i,j in enumerate(nums):
            diff = target - j
            if diff in pair:
                return [pair[diff],i]
            pair[j] =i
        return 

        