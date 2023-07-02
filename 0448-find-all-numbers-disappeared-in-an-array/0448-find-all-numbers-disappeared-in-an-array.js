/**
 * @param {number[]} nums
 * @return {number[]}
 */
var findDisappearedNumbers = function(nums) {
    
    let nums_new = nums.sort((a,b) => a - b).filter((elements, index) => {
        return nums.indexOf(elements) === index;
    });
    let tmp = [];
    let i = 1;
    let index = 0;
    while (index < nums_new.length) {
        if (i == nums_new[index]) {
            i += 1;
            index += 1;
        }
        else {
            tmp.push(i);
            i += 1;
        }
    }
    if (nums.length - nums_new.length > tmp.length) {
        let h = (nums.length - nums_new.length) - tmp.length;
        let d = nums_new[nums_new.length - 1] + 1;
        while (h) {
            tmp.push(d);
            h -= 1;
            d += 1;
        }
    }
    return tmp
};
