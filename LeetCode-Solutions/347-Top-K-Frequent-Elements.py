class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for i in nums:
            freq[i] = freq.get(i,0)+1
        result=[]
        sorted_items = sorted(freq.items(), key=lambda x:x[1], reverse=True)
        for key,count in sorted_items:
            result.append(key)
            if len(result) == k:
                break
        return result
                

                

        