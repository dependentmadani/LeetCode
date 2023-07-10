/**
 * @param {number[]} height
 * @return {number}
 */
var trap = function(height) {
    let left_starter = 0;
    let right_starter = height.length - 1;
    let left_max_block = 0;
    let right_max_block = 0;
    let trapped_water = 0;

    while (left_starter < right_starter) {
        left_max_block = Math.max(left_max_block, height[left_starter])
        right_max_block = Math.max(right_max_block, height[right_starter])
        if (left_max_block < right_max_block) {
            trapped_water += left_max_block - height[left_starter]
            left_starter += 1
        }
        else {
            trapped_water += right_max_block - height[right_starter]
            right_starter -= 1
        }
    }
    return trapped_water
};
