from src.longest_uploaded_prefix import LUPrefix


def test_solution():
    server = LUPrefix(4)
    server.upload(3)
    assert server.longest() == 0
    server.upload(1)
    assert server.longest() == 1
    server.upload(2)
    assert server.longest() == 3
