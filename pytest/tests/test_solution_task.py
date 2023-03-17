from task import solution
import pytest

inp = [[-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20],  # noqa 501
       [-74, -72, -70, -67, -64, -62, -61, -60, -59, -56, -53, -52, -51, -50, -47, -44, -42, -40, -37, -36, -34, -31, -30, -29, -26, -25],  # noqa 501
       [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]]

out = ['-6,-3-1,3-5,7-11,14,15,17-20',
       '-74,-72,-70,-67,-64,-62--59,-56,-53--50,-47,-44,-42,-40,-37,-36,-34,-31--29,-26,-25',  # noqa 501
       '-3--1,2,10,15,16,18-20'
       ]

@pytest.mark.parametrize('args, expected_result', zip(inp, out))  # noqa 501
def test_solution_kata(args, expected_result):
    assert solution(args) == expected_result
