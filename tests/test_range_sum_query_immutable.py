from src.range_sum_query_immutable import NumArray


def test_num_array():
    na = NumArray([-2, 0, 3, -5, 2, -1])

    assert na.sumRange(0, 2) == 1
    assert na.sumRange(2, 5) == -1
    assert na.sumRange(0, 5) == -3
