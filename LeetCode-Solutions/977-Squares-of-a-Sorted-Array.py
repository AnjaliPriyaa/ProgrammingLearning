class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        """
        # a=[]
        # for i in nums:
        #     a.append(i**2)
        # nums = sorted(a)
        # return nums
        left = 0
        right = len(nums) - 1
        result = [0] * len(nums)

        for i in range(len(nums)-1,-1,-1):
            right_sq = nums[right] ** 2
            left_sq = nums[left] ** 2
            if left_sq > right_sq:
                result[i] = left_sq
                left+=1
            else:
                result[i] = right_sq
                right-=1
        return result



             
            


        