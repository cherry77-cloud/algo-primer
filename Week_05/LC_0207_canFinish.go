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
