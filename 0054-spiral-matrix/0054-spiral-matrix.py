class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])
"""
Python3:
def spiralOrder(self, matrix):
    return matrix and [*matrix.pop(0)] + self.spiralOrder([*zip(*matrix)][::-1])

The difference betweem Python and Python3

Python3 > Python
to improve its consistency and eliminate some of the issues in Python 2. 
Use Python3 for new project
zip() Function:

Python 2: Returned a list.
Python 3: Returns an iterator.
"""