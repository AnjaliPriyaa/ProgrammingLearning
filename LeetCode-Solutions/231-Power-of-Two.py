class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n <= 0:
        #     return False
        
        # while n > 1:
        #     if n % 2 != 0:
        #         return False
        #     n = n // 2
        # return True
            # Check if n is positive and n & (n-1) is 0
        return (n > 0) and ((n & (n - 1)) == 0)
        

        