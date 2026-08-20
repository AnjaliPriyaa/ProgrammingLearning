class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """ 
        BRUTE FORCE
        IF nums is empty:
        RETURN 0
        SORT nums
        count = 1
        max_length = 1
        FOR i from 0 to length(nums) - 2:
        IF current number == next number:
        CONTINUE                     # Ignore duplicate
        IF current number + 1 == next number:
        count = count + 1            # Continue sequence
        ELSE:
        count = 1                    # Sequence broke → start again
        max_length = MAX(max_length, count)
        RETURN max_length
        """
        if not nums: 
            return 0
        a = sorted(nums)
        count = 1
        max_len = 1
        for i in range(len(a)-1):
            if a[i] == a[i+1]:
                continue
            if a[i]+1 == a[i+1]:
                count+=1
            else:
                count = 1
            max_len = max(max_len,count)
        return max_len
        
        """ 
        OPTIMAL
        Convert nums into a SET
        max_length = 0
        FOR every number in set:
        IF number - 1 is NOT in set:       # Found START
        current_number = number
        count = 1
        WHILE current_number + 1 exists in set:
        current_number = current_number + 1
        count = count + 1
        max_length = MAX(max_length, count)
        RETURN max_length
        """


        newlist = set(nums)
        max_length = 0
        for i in newlist:
            if i-1 not in newlist:
                current_number = i
                count = 1
                while current_number + 1 in newlist:
                    current_number+=1
                    count+=1
                max_len = max(max_len,count)
        return max_len
                