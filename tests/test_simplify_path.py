import pytest

from src.simplify_path import Solution


@pytest.mark.parametrize(
    "path,expected",
    (
        ("/home/", "/home"),
        ("/home//foo/", "/home/foo"),
        ("/home/user/Documents/../Pictures", "/home/user/Pictures"),
        ("/../", "/"),
        ("/.../a/../b/c/../d/./", "/.../b/d"),
    ),
)
def test_solution(path, expected):
    assert Solution().simplifyPath(path) == expected
