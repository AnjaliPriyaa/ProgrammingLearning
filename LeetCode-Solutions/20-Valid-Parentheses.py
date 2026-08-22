class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for bracket in s:
            if bracket in "{[(":
                stack.append(bracket)
            else:
                if not stack:
                    return False
                if stack[-1] != pairs[bracket]:
                    return False
                stack.pop()
        return len(stack) == 0

                



        