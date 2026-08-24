class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Brute force / Linear scan → O(n) time, O(1) space
        # for i in letters:
        #     if i > target:
        #         return i
        # return letters[0]

        # Optimal / Binary search   → O(log n) time, O(1) space
        left = 0
        right = len(letters) - 1

        while left <= right:
            mid = (left + right) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        if left == len(letters):
            return letters[0]

        return letters[left]
       

     