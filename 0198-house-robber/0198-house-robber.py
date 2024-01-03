class Solution:
# This code snippet is a Python version of a dynamic programming solution to the
# house robber problem, where you can't rob two adjacent houses. The `prev1` and `prev2`
# variables keep track of the maximum profit from the previous houses, and the `num`
# variable represents the current house's money.
    def rob(self, nums):
        if not nums:
            return 0
        prev1 = 0
        prev2 = 0
        for num in nums:
            temp = prev1
            prev1 = max(prev2 + num, prev1)
            prev2 = temp
        return prev1
"""
def rob(nums):
    if not nums:
        return 0
    prev1 = 0
    prev2 = 0
    for num in nums:
        temp = prev1
        prev1 = max(prev2 + num, prev1)
        prev2 = temp
    return prev1

Cause runtime error, it seems like is becasue there is not self.
In Python, the self keyword is used in object-oriented programming to refer to the instance of the current class. It allows access to the attributes and methods of the class in Python. When you create a new instance of a class, self refers to that specific instance.
"""


        
        