from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        '''
        https://leetcode.com/problems/counting-bits/description/
        Given an integer n, return an array ans of length n + 1
        such that for each i (0 <= i <= n), ans[i] is the number
        of 1's in the binary representation of i.
        '''
        result = []
        for i in range(n + 1):
            result += [0]
            while i > 0:
                if i % 2:
                    result[-1] += 1
                i //= 2
        return result
