func groupAnagrams(strs []string) [][]string {
    anagramsMap := map[string][]string{}
    for _, str := range strs {
        sortedBytes := []byte(str)          // 将字符串转换为字节切片
        slices.Sort(sortedBytes)            // 对字节切片进行排序
        sortedStr := string(sortedBytes)    // 将排序后的字节切片转换回字符串

        // 将排序后的字符串作为键，原字符串作为值，添加到 map 中
        anagramsMap[sortedStr] = append(anagramsMap[sortedStr], str)
    }

    return slices.Collect(maps.Values(anagramsMap))
}
