class Solution:
    MOD = 1337

    def superPow(self, a: int, b: list[int]) -> int:
        if not b:
            return 1
        last = b.pop()
        part1 = pow(a, last, self.MOD)
        part2 = pow(self.superPow(a, b), 10, self.MOD)
        return (part1 * part2) % self.MOD
