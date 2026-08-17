class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height) - 1
        max_water = 0
        
        while left < right:
            # Calculate width and current capacity
            width = right - left
            current_water = min(height[left], height[right]) * width
            
            # Update maximum water found so far
            max_water = max(max_water, current_water)
            
            # Move the pointer with the smaller height
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
                
        return max_water
