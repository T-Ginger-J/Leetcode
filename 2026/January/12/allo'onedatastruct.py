class AllOne:

    def __init__(self):
        self.key_count = {}  # key -> count
        self.count_bucket = {}  # count -> bucket
        self.head = Bucket(float('-inf'))
        self.tail = Bucket(float('inf'))
        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert_bucket_after(self, new_bucket, prev_bucket):
        new_bucket.prev = prev_bucket
        new_bucket.next = prev_bucket.next
        prev_bucket.next.prev = new_bucket
        prev_bucket.next = new_bucket

    def _remove_bucket(self, bucket):
        bucket.prev.next = bucket.next
        bucket.next.prev = bucket.prev
        del self.count_bucket[bucket.count]

    def inc(self, key: str) -> None:
        old_count = self.key_count.get(key, 0)
        new_count = old_count + 1
        self.key_count[key] = new_count

        old_bucket = self.count_bucket.get(old_count)
        new_bucket = self.count_bucket.get(new_count)
        if not new_bucket:
            new_bucket = Bucket(new_count)
            self.count_bucket[new_count] = new_bucket
            if old_count == 0:
                self._insert_bucket_after(new_bucket, self.head)
            else:
                self._insert_bucket_after(new_bucket, old_bucket)
        new_bucket.keys.add(key)

        if old_bucket:
            old_bucket.keys.remove(key)
            if len(old_bucket.keys) == 0:
                self._remove_bucket(old_bucket)

    def dec(self, key: str) -> None:
        if key not in self.key_count:
            return
        old_count = self.key_count[key]
        old_bucket = self.count_bucket[old_count]
        old_bucket.keys.remove(key)

        if old_count == 1:
            del self.key_count[key]
        else:
            new_count = old_count - 1
            self.key_count[key] = new_count
            new_bucket = self.count_bucket.get(new_count)
            if not new_bucket:
                new_bucket = Bucket(new_count)
                self.count_bucket[new_count] = new_bucket
                self._insert_bucket_after(new_bucket, old_bucket.prev)
            new_bucket.keys.add(key)

        if len(old_bucket.keys) == 0:
            self._remove_bucket(old_bucket)

    def getMaxKey(self) -> str:
        return next(iter(self.tail.prev.keys)) if self.tail.prev != self.head else ""

    def getMinKey(self) -> str:
        return next(iter(self.head.next.keys)) if self.head.next != self.tail else ""

