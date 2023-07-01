/**
 * @param {number[]} nums
 * @return {boolean}
 */
var containsDuplicate = function(nums) {
    let a = 0;
    for (i in nums) {
        a = nums[i];
        var tmp = nums.filter(value => value == a);
        if (tmp.length > 1)
            return true;
    }
    return false;
};
