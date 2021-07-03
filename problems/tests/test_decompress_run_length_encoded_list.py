import pytest
from src.decompress_run_length_encoded_list import Solution


@pytest.mark.parametrize(
    "nums,decompressed_list",
    [
        ([1, 2, 3, 4], [2, 4, 4, 4]),
        ([1, 1, 2, 3], [1, 3, 3]),
        ([1, 1, 1, 2, 1, 3], [1, 2, 3]),
    ],
)
def test_solution(nums, decompressed_list):
    assert Solution().decompressRLElist(nums) == decompressed_list
