# LeetCode 460: LFU Cache
# Explanation:
# Implement an LFU (Least Frequently Used) cache:
# - get(key): return value and update frequency
# - put(key, value): insert/update value, evict least frequently used if capacity exceeded
#
# Method 1: Hash + Doubly Linked List (Optimal)
# - Use:
#   1. key -> (value, freq) mapping
#   2. freq -> ordered dict (keys in order of use)
#   3. Track min frequency
# - On get/put, update frequency, move key to new freq list
#
# Time Complexity: O(1) per operation
# Space Complexity: O(capacity)

from collections import defaultdict, OrderedDict

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_to_val_freq = {}  # key -> (val, freq)
        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> keys
        self.min_freq = 0

    def _update_freq(self, key):
        val, freq = self.key_to_val_freq[key]
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
        self.key_to_val_freq[key] = (val, freq + 1)
        self.freq_to_keys[freq + 1][key] = None

    def get(self, key: int) -> int:
        if key not in self.key_to_val_freq:
            return -1
        self._update_freq(key)
        return self.key_to_val_freq[key][0]

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_to_val_freq:
            self.key_to_val_freq[key] = (value, self.key_to_val_freq[key][1])
            self._update_freq(key)
            return
        if len(self.key_to_val_freq) >= self.capacity:
            # Evict least frequently used, oldest key
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val_freq[evict_key]
        self.key_to_val_freq[key] = (value, 1)
        self.freq_to_keys[1][key] = None
        self.min_freq = 1


# Additional Examples

# Example 1: Basic operations
lfu = LFUCache(2)
lfu.put(1,1)
lfu.put(2,2)
print(lfu.get(1))  # Expected 1
lfu.put(3,3)       # Evicts key 2
print(lfu.get(2))  # Expected -1
print(lfu.get(3))  # Expected 3

# Example 2: Update frequency
lfu2 = LFUCache(2)
lfu2.put(1,1)
lfu2.put(2,2)
lfu2.get(1)        # freq of 1 becomes 2
lfu2.put(3,3)      # Evicts key 2 (freq=1)
print(lfu2.get(1)) # Expected 1
print(lfu2.get(2)) # Expected -1
print(lfu2.get(3)) # Expected 3

# Example 3: Capacity zero
lfu3 = LFUCache(0)
lfu3.put(1,1)
print(lfu3.get(1)) # Expected -1
