#53. Maximum Subarray

nums  = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
#Brute Force - Trying out all the combination - O(n³) → brute force
# maximum_sum = negative infinity
# FOR i from 0 to n-1:                 # i → WHERE does subarray START?
# FOR j from i to n-1:             # j → WHERE does subarray END?
# sum = 0
# FOR k from i to j:           # k → ADD everything from START to END
# sum = sum + array[k]
# maximum_sum = max(maximum_sum, sum)
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
# sum = 0
# FOR every number:
# add number to sum
# update max_sum
# IF sum becomes negative:
# reset sum to 0
# RETURN max_sum

#we need the which elements gave me maximum sum?
    # maximum_sum = float("-inf")
    # sum = 0
    # for i in nums: 
    #     sum+=i
    #     if sum > maximum_sum:
    #         maximum_sum = sum
    #     if sum < 0:
    #         sum = 0
    # return maximum_sum

    maximum_sum = float("-inf")
    sum = 0
    start = 0
    ans_start = -1
    ans_end = -1
    for i in range(len(nums)):
        # We are starting a new candidate subarray
        if sum == 0:
            start = i

        sum += nums[i]

        # Found a better subarray
        if sum > maximum_sum:
            maximum_sum = sum
            ans_start = start
            ans_end = i

        # Negative sum will hurt future elements,
        # so discard this subarray and start fresh
        if sum < 0:
            sum = 0

    return maximum_sum, nums[ans_start:ans_end + 1]

print(maxSubArray(nums))