/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var findKthLargest = function(nums, k) {
    nums.sort((a, b) => b - a);

    tmp = []
    for (let i = 0; i < k; ++ i) {
        tmp.push(nums[i])
    }
    return tmp[tmp.length - 1]
};
