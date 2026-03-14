Palindrome Substring Checker

Given a string, determine if there exists a substring within the string that is a palindrome of length greater than 1. A palindrome is a string that reads the same backward as forward. Your task is to check for any such substring and return 'YES' if it exists, otherwise return 'NO'.

Input
A single line containing a string s consisting of lowercase English letters.
Output
Output 'YES' if there exists a palindrome substring of length greater than 1, otherwise output 'NO'.

Constraints - 1 <= s.length <= 100000

Hint
Consider using a nested loop to generate all possible substrings and check if any of them is a palindrome. Remember, you only need to check substrings of length greater than 1.
