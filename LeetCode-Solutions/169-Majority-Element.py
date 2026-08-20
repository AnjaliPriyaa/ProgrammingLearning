class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = {}
        for i in nums:
            frequency[i] = frequency.get(i,0)+1
        max_element = max(frequency,key=frequency.get)
        return max_element
        