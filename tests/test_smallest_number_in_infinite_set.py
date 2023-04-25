from src.smallest_number_in_infinite_set import SmallestInfiniteSet


def test_solution():
    st = SmallestInfiniteSet()
    st.addBack(2)

    assert st.popSmallest() == 1
    assert st.popSmallest() == 2
    assert st.popSmallest() == 3

    st.addBack(1)
    st.addBack(1)

    assert st.popSmallest() == 1
    assert st.popSmallest() == 4
    assert st.popSmallest() == 5
