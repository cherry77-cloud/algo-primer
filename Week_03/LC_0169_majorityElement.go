func majorityElement(nums []int) int {
    count := 0
    var candidate int
    for _, num := range nums {
        if count == 0 {
            candidate = num
        }
        if candidate == num {
            count += 1
        } else {
            count -= 1
        }
    }
    return candidate
}
