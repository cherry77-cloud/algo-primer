```cpp
class MedianFinder {
private:
    priority_queue<int> left;  // 大根堆
    priority_queue<int, vector<int>, greater<>> right;
public:
    MedianFinder() {}
    
    void addNum(int num) {
        if (left.size() == right.size()) {
            right.push(num);
            left.push(right.top());
            right.pop();
        } else {
            left.push(num);
            right.push(left.top());
            left.pop();
        }
    }
    
    double findMedian() {
        if (left.size() > right.size()) {
            return left.top();
        }
        return (left.top() + right.top()) / 2.0;
    }
};
```

---

