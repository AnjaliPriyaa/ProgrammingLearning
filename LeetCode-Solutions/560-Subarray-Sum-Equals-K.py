class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:   
        # result = []
        # for i in range(len(nums)):
        #     total = nums[i]
        #     for j in range(i+1,len(nums)):
        #         total += nums[j]
        #         if total == k:
        #             result.append(tuple(nums[i:j+1]))
        #     if nums[i] == k:
        #         result.append((nums[i],None))
        # return len(result)  
        prefix_count = {0:1}
        prefix_sum = 0
        count = 0
        for i in nums:
            prefix_sum += i
            needed = prefix_sum - k
            if needed in prefix_count:
                count+=prefix_count[needed]
            prefix_count[prefix_sum] = (prefix_count.get(prefix_sum, 0) + 1)

        return count


         


        