from typing import List, Optional
from medium import ListNode


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

    def singleNumber(self, nums: List[int]) -> int:
        '''
        https://leetcode.com/problems/single-number/description/
        Given a non-empty array of integers nums, every element
        appears twice except for one. Find that single one.
        '''
        r = 0
        for i in nums:
            r = i ^ r
        return r

    def isAnagram(self, s: str, t: str) -> bool:
        '''
        https://leetcode.com/problems/valid-anagram/description/
        Given two strings s and t, return true if t
        is an anagram of s, and false otherwise.
        '''
        if len(t) != len(s):
            return False
        return sorted(s) == sorted(t)

    def addBinary(self, a: str, b: str) -> str:
        '''
        https://leetcode.com/problems/add-binary/description/
        Given two binary strings a and b,
        return their sum as a binary string.
        '''
        # extra = 0
        # result = ''
        # len_a = len(a)
        # len_b = len(b)
        # if len_a != len_b:
        #     longest = len(max(a, b, key=len))
        #     if len_a < longest:
        #         a = '0' * (longest - len_a) + a
        #     elif len_b < longest:
        #         b = '0' * (longest - len_b) + b
        # for i, j in zip(a[::-1], b[::-1]):
        #     num = int(i) + int(j) + extra
        #     if num > 1:
        #         result += str(num - 2)
        #         extra = 1
        #         continue
        #     result += str(num)
        #     extra = 0
        # while extra:
        #     result += '1'
        #     extra -= 1
        # return result[::-1]
        return bin(int(a, 2) + int(b, 2))[2:]

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        https://leetcode.com/problems/greatest-common-divisor-of-strings/
        For two strings s and t, we say "t divides s" if and
        only if s = t + ... + t (i.e., t is concatenated with
        itself one or more times).
        '''
        # longest = max(str1, str2, key=len)
        # long = ''
        # for i in range(len(longest)):
        #     for j in range(len(longest)):
        #         str1_r = str1.replace(longest[i:j], '')
        #         str2_r = str2.replace(longest[i:j], '')
        #         if not str1_r and not str2_r:
        #             if len(long) < len(longest[i:j]):
        #                 long = longest[i:j]
        # return long
        # if str1.replace(str2, '') == '':
        #     return str2
        shortest = min(str1, str2, key=len)
        longest = max(str1, str2, key=len)
        if not longest.replace(shortest, ''):
            return shortest
        for i in range(len(shortest), 0, -1):
            if not shortest.replace(str1[i:], ''):
                if longest.replace(str1[i:], ''):
                    continue
                else:
                    return longest[i:]
        return ''

    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        https://leetcode.com/problems/merge-strings-alternately/description/
        You are given two strings word1 and word2. Merge the strings by adding
        letters in alternating order, starting with word1. If a string is
        longer than the other, append the additional letters onto the end of
        the merged string.
        '''
        longest = len(max(word1, word2, key=len))
        result = ''
        for i in range(longest):
            result += word1[i:i + 1] + word2[i:i + 1]
        return result

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        https://leetcode.com/problems/middle-of-the-linked-list/description/
        Given the head of a singly linked list, return the list node from the
        middle.
        '''
        nodes = []
        while head:
            nodes += [head.val]
            head = head.next
        length = len(nodes)
        if length % 2 != 0:
            nodes = nodes[length // 2 + 1:]
        else:
            nodes = nodes[length // 2:]
        new_head = ListNode(nodes.pop(0))
        head = new_head
        while nodes:
            new_head.next = ListNode(nodes.pop(0))
            new_head = new_head.next
        return head
