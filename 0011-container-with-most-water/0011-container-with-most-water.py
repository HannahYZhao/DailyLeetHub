class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        maxArea = 0

        # Enter a loop using the condition left < right, which means the pointers have not crossed each other yet
        while left < right:
            currentArea = min(height[left], height[right]) * (right - left)
            # If the currentArea is greater than the maxArea, update maxArea with the currentArea
            maxArea = max(maxArea, currentArea)

            '''
            Move the pointers inward: (Explained in detail below)
            Check if the height at the left pointer is smaller than the height at the right pointer.
            If so, increment the left pointer, moving it towards the center of the container.
            Otherwise, decrement the right pointer, also moving it towards the center.
            '''
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1                  # Repeat steps 3 to 5 until the pointers meet (left >= right Indicating that all possible containers have been explored
        
        return maxArea