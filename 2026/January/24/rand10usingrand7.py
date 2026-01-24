import random

def rand7():
    return random.randint(1, 7)

class Solution:
    def rand10(self) -> int:
        while True:
            num = (rand7() - 1) * 7 + rand7()  # 1..49
            if num <= 40:
                return (num - 1) % 10 + 1

