import pytest

from src.find_duplicate_file_in_system import Solution


@pytest.mark.parametrize(
    "paths,expected",
    [
        (
            [
                "root/a 1.txt(abcd) 2.txt(efgh)",
                "root/c 3.txt(abcd)",
                "root/c/d 4.txt(efgh)",
                "root 4.txt(efgh)",
            ],
            [
                ["root/a/1.txt", "root/c/3.txt"],
                ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"],
            ],
        ),
        (
            [
                "root/a 1.txt(abcd) 2.txt(efgh)",
                "root/c 3.txt(abcd)",
                "root/c/d 4.txt(efgh)",
            ],
            [
                ["root/a/1.txt", "root/c/3.txt"],
                ["root/a/2.txt", "root/c/d/4.txt"],
            ],
        ),
    ],
)
def test_solution(paths, expected):
    assert Solution().findDuplicate(paths) == expected
