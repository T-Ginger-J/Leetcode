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

