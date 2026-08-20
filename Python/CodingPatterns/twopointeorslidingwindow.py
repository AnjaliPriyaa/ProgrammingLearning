#4 shorts of coding patterns
# First - when it is a constant window.
#question max sum you can obtain by picking up 4 elemenst consecutively

# 1. Create first window of size k
# 2. Calculate its sum
# 3. Save it as the current answer

# Then repeatedly:

# REMOVE arr[left]
# MOVE left
# MOVE right
# ADD arr[right]
# UPDATE answer
# [-1, 2, 3, 3]       → 7
#      [2, 3, 3, 4]    → 12
#         [3, 3, 4, 5] → 15 
#            [3, 4, 5, -1] → 11

# Maximum = 15


arr = [-1,2,3,3,4,5,-1]
k = 4
def maxtotalofk(arr,k):
    # Length of the array
    n = len(arr)

    # Initialize the window
    # left points to the first element of the window
    # right points to the last element of the window
    left = 0
    right = k - 1

    # Calculate the sum of the first window
    total = 0

    for i in range(k):
        total += arr[i]

    # Initially, the first window sum is our maximum
    max_sum = total

    # Slide the window until right reaches the end of the array
    while right < n - 1:

        # Remove the element that is leaving the window
        total -= arr[left]

        # Move both pointers one position forward
        left += 1
        right += 1

        # Add the new element entering the window
        total += arr[right]

        # Compare current window sum with maximum found so far
        max_sum = max(max_sum, total)

    # Return the maximum sum of any k consecutive elements
    return max_sum
print(maxtotalofk(arr,k))



#Second Pattern - Longest Substring/subarray where some condition
# condition - k<=14
arr = [2,5,1,7,10]
k = 14
max_length = 0
for i in range(len(arr)):
    sum = 0
    for j in range(i,len(arr)):
        sum += arr[j]
        if sum <= k:
            max_length = max(max_length, j-i+1)
        elif sum > k:
            break
print(max_length)



