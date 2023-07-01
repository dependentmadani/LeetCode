/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    nums.sort((a, b) => a - b);
    console.log(nums)

    if (nums[0] != 0)
        return 0;

    for (i in nums) {
        if (i != nums[i]) 
            return i;
    }
    return nums.length;
};
