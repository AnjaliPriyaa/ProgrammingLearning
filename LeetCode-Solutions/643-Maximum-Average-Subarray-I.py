class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        left = 0
        right = k-1
        total = 0
        for i in range(k):
            total+=nums[i]
        max_sum =  total
        while (right < n-1):
            total-=nums[left]
            left+=1
            right+=1
            total+=nums[right]
            max_sum = max(max_sum,total)
        return max_sum/k
