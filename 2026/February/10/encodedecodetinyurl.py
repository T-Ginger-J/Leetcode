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


# -------------------------------------------------------
# Examples (Including Edge Cases)
# -------------------------------------------------------

codec = Codec()

# Example 1
url1 = "https://leetcode.com/problems/design-tinyurl"
short1 = codec.encode(url1)
print(short1)                  # http://tinyurl.com/1
print(codec.decode(short1))    # original URL

# Example 2 (Multiple URLs)
url2 = "https://openai.com/research"
short2 = codec.encode(url2)
print(short2)                  # http://tinyurl.com/2
print(codec.decode(short2))    # original URL

# Example 3 (Repeated URL)
short3 = codec.encode(url1)
print(short3)                  # http://tinyurl.com/3
print(codec.decode(short3))    # url1

# Example 4 (Invalid decode)
print(codec.decode("http://tinyurl.com/999"))  # ""

# Example 5 (Empty URL)
short5 = codec.encode("")
print(short5)                  # http://tinyurl.com/4
print(codec.decode(short5))    # ""
