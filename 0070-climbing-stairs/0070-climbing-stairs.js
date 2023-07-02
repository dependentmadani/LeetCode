/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let prev_1 = 1;
    let prev_2 = 0;

    for (let i = 1; i < n + 1; i++) {
        let current = prev_1 + prev_2;

        prev_2 = prev_1;
        prev_1 = current;
    }

    return prev_1
};
