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

    def longestPalindrome(self, s: str) -> int:
        length = len(s)
        max = 0
        for i in range(length):
            for j in range(i, length):
                substr = s[i:j]
                if substr == substr[::-1]:
                    now = len(substr)
                    if now > max:
                        max = now
        return max

    def checkPerfectNumber(self, num: int) -> bool:
        '''
        https://leetcode.com/problems/perfect-number/
        A perfect number is a positive integer that
        is equal to the sum of its positive divisors,
        excluding the number itself. A divisor of an
        integer x is an integer that can divide x evenly.
        Given an integer n, return true if n is a perfect
        number, otherwise return false.
        '''
        result = 1
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                result += i
                print(i)
        return num == result

    def lengthOfLastWord(self, s: str) -> int:
        '''
        https://leetcode.com/problems/length-of-last-word/description/
        Given a string s consisting of words and spaces,
        return the length of the last word in the string.
        '''
        return len(s.split()[-1])


a = Solution()
print(a.checkPerfectNumber(99999993))
