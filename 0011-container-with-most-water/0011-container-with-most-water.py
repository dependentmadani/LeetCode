class Solution:
    def maxArea(self, height: List[int]) -> int:
        required_area = 0
        left_side = 0
        right_side = len(height) - 1
        difference = right_side - left_side
        while difference > 0:
            required_area = max(required_area, min(height[left_side], height[right_side]) * difference)
            if (height[left_side] <= height[right_side]):
                left_side += 1
            elif (height[left_side] > height[right_side]):
                right_side -= 1
            difference = right_side - left_side
        
        return required_area
            