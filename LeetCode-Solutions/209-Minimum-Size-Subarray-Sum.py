class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        total = 0
        min_len = len(nums) + 1

        for right in range(len(nums)):

            total += nums[right]
            # print(total)
            while total >= target:

                length = right - left + 1
                min_len = min(min_len, length)

                total -= nums[left]
                left += 1

        if min_len == len(nums) + 1:
            return 0

        return min_len
