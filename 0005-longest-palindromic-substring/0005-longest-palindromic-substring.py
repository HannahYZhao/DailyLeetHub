'''
Optimizations and improvements made:

-Removed unnecessary variables and made the code more readable.
-Eliminated the inner loop, which reduces the time complexity.
-Improved the way palindrome substrings are tracked in the dp table.
-Improved the way the start and length of the longest palindrome are determined.
-Handled palindromes of different lengths in a more systematic way.
-This optimized code should perform better and be more readable while still solving the problem effectively.
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        
        # Initialize a 2D table to track palindrome substrings
        dp = [[False] * n for _ in range(n)]

        start = 0  # Start index of the longest palindrome found
        maxLen = 1  # Length of the longest palindrome found

        # All single characters are palindromes
        for i in range(n):
            dp[i][i] = True

        # Check for palindromes of length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                maxLen = 2

        # Check for palindromes of length 3 or more
        for length in range(3, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = True
                    if length > maxLen:
                        start = i
                        maxLen = length

        return s[start : start + maxLen]
