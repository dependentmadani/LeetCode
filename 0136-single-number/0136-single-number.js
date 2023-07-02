/**
 * @param {number[]} nums
 * @return {number}
 */
var singleNumber = function(nums) {
    nums.sort((a, b) => a-b);

    let nums_only_repeated = nums.filter((elements, index) => {
        return nums.indexOf(elements) !== index;
    })


    let single_num = nums.filter(x => !nums_only_repeated.includes(x))

    return single_num[0];
};
