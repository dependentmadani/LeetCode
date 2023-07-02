/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let len = prices.length;

    let profit = 0
    let hold_stock = prices[0]

    for (let i = 1; i < len; i++ ) {
        hold_stock = Math.min(hold_stock, prices[i]);
        profit = Math.max(profit, prices[i] - hold_stock)
    }

    return profit
}
