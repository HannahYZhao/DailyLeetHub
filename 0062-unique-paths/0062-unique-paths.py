# Time Complexity: O(m) or O(n)
# Space Complexity: O(1)
'''
Combinatorial Mathematics
Intuition
The number of unique paths can be seen as the number of ways to choose m−1 downs and n−1 rights, regardless of the order. In combinatorial terms, this is equivalent to(m + n - 2 to m - 1)
Algorithm
1. Use the combinatorial formula:
   (m + n - 2 to m - 1) or (m + n - 2 to n - 1) to calculate the number of unique paths.
2. Python's Math Library:
   Python provides a built-in function math.comb(n, k) to talculate(n to k) efficiently. 
'''
import math

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.comb(n + m - 2, n - 1)