/**
 * @param {number[]} nums
 * @return {number[][]}
 */
var threeSum = function(nums) {
    nums = nums.sort((a, b) => a - b);
    var result = []
    var l = 0;
    var r = 0;
    var total_sum = 0;

    for (let i = 0; i < nums.length; ++i) {
        if (i > 0 && nums[i] === nums[i - 1]) {
            continue ;
        }
        l = i + 1;
        r = nums.length - 1;
        while (l < r) {
            total_sum = nums[i] + nums[l] + nums[r];
            if (total_sum > 0) {
                r -= 1
            }
            else if (total_sum < 0) {
                l += 1
            }
            else {
                result.push([nums[i], nums[l], nums[r]]);
                l += 1
                while (nums[l] === nums[l - 1] && l < r) {
                    l += 1
                }
            }
        }
    }
    return result
};
