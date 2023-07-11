from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            result += [0]
            while i > 0:
                if i % 2:
                    result[-1] += 1
                i //= 2
        return result
