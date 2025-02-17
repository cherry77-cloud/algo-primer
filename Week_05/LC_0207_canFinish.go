func canFinish(numCourses int, prerequisites [][]int) bool {
    indegrees := make([]int, numCourses)
    adjacency := make([][]int, numCourses)
    queue := []int{}
    // 构建入度数组和邻接表
    for _, pre := range prerequisites {
        cur, preCourse := pre[0], pre[1]
        indegrees[cur]++
        adjacency[preCourse] = append(adjacency[preCourse], cur)
    }
    // 将所有入度为0的课程加入队列
    for i := 0; i < numCourses; i++ {
        if indegrees[i] == 0 {
            queue = append(queue, i)
        }
    }
    // BFS遍历
    for len(queue) > 0 {
        pre := queue[0]
        queue = queue[1:] // 从队列中取出课程
        numCourses-- // 处理一个课程
        // 对于该课程的所有后续课程，减少它们的入度
        for _, cur := range adjacency[pre] {
            indegrees[cur]--
            if indegrees[cur] == 0 {
                queue = append(queue, cur) // 如果入度为0，加入队列
            }
        }
    }
    // 如果所有课程都能被完成，numCourses会减少到0
    return numCourses == 0
}


func canFinish(numCourses int, prerequisites [][]int) bool {
    g := make([][]int, numCourses)
    for _, p := range prerequisites {
        g[p[1]] = append(g[p[1]], p[0])
    }

    colors := make([]int, numCourses)
    var dfs func(int) bool
    dfs = func(x int) bool {
        colors[x] = 1        // x 正在访问中
        for _, y := range g[x] {
            if colors[y] == 1 || colors[y] == 0 && dfs(y) {
                return true  // 找到了环
            }
        }
        colors[x] = 2        // x 完全访问完毕
        return false         // 没有找到环
    }

    for i, c := range colors {
        if c == 0 && dfs(i) {
            return false     // 有环
        }
    }
    return true              // 没有环
}
