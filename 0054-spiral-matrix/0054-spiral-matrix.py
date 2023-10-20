class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        rows, cols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, rows - 1, 0, cols - 1
        result = []
        # To traverse each layer, we need to keep track of the four boundaries of the current spiral
        while len(result) < rows * cols:
            for i in range(left, right + 1):
                # Add the elements to the result list
                """
                The append() function in Python takes a single item as an input parameter and adds it to the end of the given list. In Python, append() doesn't return a new list of items; in fact, it returns no value at all.
                
                fruits = ["apple", "banana", "cherry"]
                fruits.append("orange")
                print(fruits)
                """
                result.append(matrix[top][i])
            # From left move to the right
            top += 1

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            # From right move to the left
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1
            
            if left <= right:
                for i in range(bottom, top - 1,  -1):
                    result.append(matrix[i][left])
                left += 1
            
        return result