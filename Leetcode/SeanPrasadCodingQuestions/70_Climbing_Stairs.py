class Solution:
    def climbStairs(self, n: int) -> int:
# Brute force
        # prev = 1
        # prevlast = 0
        # total = 1

        # for i in range(n):
        #     total = prev + prevlast
        #     prevlast = prev
        #     prev = total
        # return total

        def sumtotal(n, store = {}):
            if n<=1:
             return 1
            if n < 0:
             return 0

            if n in store:
                return store[n]
            
            store[n] = sumtotal(n-2) + sumtotal(n-1)
            return store[n]
        return sumtotal(n
