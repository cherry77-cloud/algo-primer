func maxProfit(prices []int) int {
    minPrice, ans := prices[0], 0
    for _, price := range prices {
        minPrice = min(minPrice, price)
        ans = max(ans, price - minPrice)
    }
    return ans
}
