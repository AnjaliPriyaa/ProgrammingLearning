class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        declare a dictionary
        adding elements of nums to it, and inc the count
        condition check for value which one is equal to 1
        Will return that key.
        """
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        for key, value in freq.items():
            if value == 1:
                return key


