/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(numbers, target) {
    let result = [0, 0]
    let starter_left = 0;
    let starter_right = numbers.length - 1;
    let sum = 0;

    while (starter_left < starter_right) {
        sum = numbers[starter_left] + numbers[starter_right]
        if (sum === target) {
            result[0] = starter_left + 1;
            result[1] = starter_right + 1;
            return result
        }
        else if (sum < target) {
            starter_left += 1;
        }
        else {
            starter_right -= 1;
        }
    }
    return result
};
