import pytest

from src.serialize_and_deserialize_binary_tree import Codec
from src.utils.binary_tree import list_to_tree
from src.utils.binary_tree import tree_to_list


@pytest.mark.parametrize(
    "in_list",
    [
        ([1, 2, 3, None, None, 4, 5]),
        (
            [
                4,
                -7,
                -3,
                None,
                None,
                -9,
                -3,
                9,
                -7,
                -4,
                None,
                6,
                None,
                -6,
                -6,
                None,
                None,
                0,
                6,
                5,
                None,
                9,
                None,
                None,
                -1,
                -4,
                None,
                None,
                None,
                -2,
            ]
        ),
    ],
)
def test_codec(in_list):
    root = list_to_tree(in_list)

    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))
    assert tree_to_list(ans) == in_list
