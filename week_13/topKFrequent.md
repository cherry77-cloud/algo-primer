```cpp
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> cnt;
        for (auto& v : nums) {
            cnt[v] += 1;
        }
        
        auto cmp = [](const pair<int, int>& a, const pair<int, int>& b) {
            return a.second > b.second;
        };
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> heap(cmp);

        for (auto& [num, count] : cnt) {
            if (heap.size() < k) {
                heap.emplace(num, count);
            } else if (count > heap.top().second) {
                heap.pop();
                heap.emplace(num, count);
            }
        }

        vector<int> ret;
        while (!heap.empty()) {
            ret.emplace_back(heap.top().first);
            heap.pop();
        }
        return ret;
    }
};
```

---

```go
func topKFrequent(nums []int, k int) []int {
    occurrences := map[int]int{}
    for _, num := range nums {
        occurrences[num]++
    }

    h := &IHeap{}
    heap.Init(h)
    for key, value := range occurrences {
        heap.Push(h, [2]int{key, value});
        if h.Len() > k {
            heap.Pop(h)
        }
    }

    ret := make([]int, k)
    for i := 0; i < k; i++ {
        ret[k - i - 1] = heap.Pop(h).([2]int)[0]
    }
    return ret
}

type IHeap [][2]int

func (h IHeap) Len() int { 
    return len(h) 
}

func (h IHeap) Less(i, j int) bool { 
    return h[i][1] < h[j][1] 
}

func (h IHeap) Swap(i, j int) {
    h[i], h[j] = h[j], h[i]
}

func (h *IHeap) Push (x interface{}) {
    *h = append(*h, x.([2]int))
}

func (h *IHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n - 1]
    *h = old[0 : n-1]
    return x
}
```
