class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    #Brute Force - Trying out all the combination - O(n³) → brute force
    # maximum_sum = negative infinity
    # FOR i from 0 to n-1:                 # i → WHERE does subarray START?
    # FOR j from i to n-1:             # j → WHERE does subarray END?
    # current_sum = 0
    # FOR k from i to j:           # k → ADD everything from START to END
    # current_sum = current_sum + array[k]
    # maximum_sum = max(maximum_sum, current_sum)
    # RETURN maximum_sum

        # maximum_sum = float("-inf")
        # for i in range(len(nums)):
        #     for j in range(i,len(nums)):
        #         sum = 0
        #         for k in range(i,j+1):
        #             sum += nums[k]
        #             maximum_sum = max(maximum_sum,sum)
        # return maximum_sum

    #Better Solution - O(n²) → reuse previous subarray sum
        # O(n³) BRUTE FORCE
        # i → START
        # j → END
        # k → SUM i through j
        # O(n²) BETTER
        # i → START
        # j → END + keep adding nums[j]
        # No k loop because:
        # new_sum = previous_sum + nums[j]

        # maximum_sum = float("-inf")
        # for i in range(len(nums)):
        #     sum = 0
        #     for j in range(i,len(nums)):
        #         sum += nums[j]
        #         maximum_sum = max(maximum_sum,sum)
        # return maximum_sum

    #OPTIMAL Solution
    # max_sum = negative infinity
    # current_sum = 0
    # FOR every number:
    # add number to current_sum
    # update max_sum
    # IF current_sum becomes negative:
    # reset current_sum to 0
    # RETURN max_sum
    
        maximum_sum = float("-inf")
        sum = 0
        for i in nums: 
            sum+=i
            if sum > maximum_sum:
                maximum_sum = sum
            if sum < 0:
                sum = 0
        return maximum_sum