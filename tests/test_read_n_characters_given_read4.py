import itertools
from unittest.mock import patch

import pytest

from src.read_n_characters_given_read4 import Solution

MOCK_TARGET = "src.read_n_characters_given_read4.read4"


@pytest.mark.parametrize(
    "file_content,n,expected_read,expected_buf",
    (
        ("abc", 4, 3, "abc"),
        ("abcde", 5, 5, "abcde"),
        ("abcdABCD1234", 12, 12, "abcdABCD1234"),
    ),
)
def test_solution(file_content, n, expected_read, expected_buf):
    call_result = itertools.batched(file_content, 4)

    def fake_read4(buf4: list[str]) -> int:
        try:
            batch = list(next(call_result))
            buf4[:] = batch
            return len(batch)
        except StopIteration:
            return 0

    buf = [""] * n

    with patch(MOCK_TARGET, new=fake_read4):
        assert Solution().read(buf, n) == expected_read
        assert "".join(buf) == expected_buf
