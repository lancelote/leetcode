from src.design_an_ordered_stream import OrderedStream


def test_ordered_stream():
    stream = OrderedStream(5)

    assert stream.insert(3, "c") == []
    assert stream.insert(1, "a") == ["a"]
    assert stream.insert(2, "b") == ["b", "c"]
    assert stream.insert(5, "e") == []
    assert stream.insert(4, "d") == ["d", "e"]
