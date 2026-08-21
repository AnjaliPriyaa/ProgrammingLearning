class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = set()
        for i in range(len(nums)):
            seen = set()
            for j in range(i+1,len(nums)):
                k = -(nums[i]+nums[j])
                if k in seen:
                    temp = [nums[i], nums[j],k]
                    temp.sort()
                    result.add(tuple(temp))    
                seen.add(nums[j])
        answer = []
        for item in result:
            answer.append(list(item))
        return answer