// LeetCode 146: LRU Cache
// Explanation:
// 1. Use unordered_map for O(1) key lookup.
// 2. Use list for maintaining usage order (front = most recent).
// 3. Move used items to front; evict least recent when over capacity.
// Time Complexity: O(1)
// Space Complexity: O(capacity)

#include <unordered_map>
#include <list>
using namespace std;

class LRUCache {
    int cap;
    list<pair<int, int>> cache;
    unordered_map<int, list<pair<int, int>>::iterator> map;
public:
    LRUCache(int capacity) : cap(capacity) {}

    int get(int key) {
        if (map.find(key) == map.end()) return -1;
        auto it = map[key];
        int value = it->second;
        cache.erase(it);
        cache.push_front({key, value});
        map[key] = cache.begin();
        return value;
    }

    void put(int key, int value) {
        if (map.find(key) != map.end()) {
            cache.erase(map[key]);
        } else if (cache.size() == cap) {
            auto del = cache.back();
            map.erase(del.first);
            cache.pop_back();
        }
        cache.push_front({key, value});
        map[key] = cache.begin();
    }
};

#include <iostream>
int main() {
    LRUCache lru(2);
    lru.put(1, 1);
    lru.put(2, 2);
    cout << lru.get(1) << endl; // Output: 1
    lru.put(3, 3);
    cout << lru.get(2) << endl; // Output: -1
    lru.put(4, 4);
    cout << lru.get(1) << endl; // Output: -1
    cout << lru.get(3) << endl; // Output: 3
    cout << lru.get(4) << endl; // Output: 4
}
