from medium import (
    Solution
)

a = Solution()


def test_threeSumClosest_1():
    result = a.threeSumClosest([-1, 2, 1, -4], 1)
    assert result == 2


def test_threeSumClosest_2():
    result = a.threeSumClosest([0, 0, 0], 1)
    assert result == 0
