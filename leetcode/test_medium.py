from leetcode.medium import (
    Solution
)

a = Solution()


def test_threeSumClosest_1():
    result = a.threeSumClosest([-1, 2, 1, -4], 1)
    assert result == 2


def test_threeSumClosest_2():
    result = a.threeSumClosest([0, 0, 0], 1)
    assert result == 0


def test_letterCombinations1():
    result = a.letterCombinations('23')
    assert result == ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]


def test_letterCombinations2():
    result = a.letterCombinations('2')
    assert result == ['a', 'b', 'c']


def test_letterCombinations3():
    result = a.letterCombinations('234')
    assert result == ["adg", "adh", "adi", "aeg", "aeh",
                      "aei", "afg", "afh", "afi", "bdg",
                      "bdh", "bdi", "beg", "beh", "bei",
                      "bfg", "bfh", "bfi", "cdg", "cdh",
                      "cdi", "ceg", "ceh", "cei", "cfg",
                      "cfh", "cfi"]
