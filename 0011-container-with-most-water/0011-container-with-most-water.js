/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    var total_area = 0
    var left_starter = 0
    var right_starter = height.length - 1
    var difference = right_starter - left_starter

    while (difference > 0) {
        total_area = Math.max(total_area, Math.min(height[left_starter], height[right_starter]) * difference)
        if (height[left_starter] <= height[right_starter])
            left_starter += 1
        else if (height[left_starter] > height[right_starter])
            right_starter -= 1
        difference = right_starter - left_starter
    }

    return total_area
};
