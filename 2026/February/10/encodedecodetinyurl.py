# LeetCode 535: Encode and Decode TinyURL
# Explanation:
# 1. Implement a system to encode a long URL into a short one, and decode it back.
# 2. Use a hash map to store mapping between short and long URLs.
# 3. Generate short URLs using a counter or random string.

# Methods Used:
# - Hash Map with Counter (Simple deterministic approach)
# - Base62 Encoding Alternative

# Time Complexity:
# - encode/decode: O(1)

# Space Complexity:
# - O(n), n = number of URLs stored


class Codec:

    # -------------------------------------------------------
    # Method 1: Counter + Hash Map (Optimal)
    # -------------------------------------------------------
    def __init__(self):
        self.counter = 0
        self.url_map = {}

    def encode(self, longUrl: str) -> str:
        self.counter += 1
        shortUrl = "http://tinyurl.com/" + str(self.counter)
        self.url_map[shortUrl] = longUrl
        return shortUrl

    def decode(self, shortUrl: str) -> str:
        return self.url_map.get(shortUrl, "")

