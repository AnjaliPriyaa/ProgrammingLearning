class Solution:
    def climbStairs(self, n: int) -> int:
        # if n == 0 or n==1:
        #     return 1

        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)
#above solution gives time limit exceeded.
        def sumtotal(n, store = {}):
            if n<=1:
             return 1
            if n < 0:
             return 0

            if n in store:
                return store[n]
            
            store[n] = sumtotal(n-2) + sumtotal(n-1)
            return store[n]
        return sumtotal(n)

            

