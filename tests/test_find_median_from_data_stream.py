from src.find_median_from_data_stream import MedianFinder


def test_solution_1():
    finder = MedianFinder()
    finder.addNum(1)
    finder.addNum(2)
    assert finder.findMedian() == 1.5
    finder.addNum(3)
    assert finder.findMedian() == 2


def test_solution_2():
    finder = MedianFinder()
    finder.addNum(-1)
    assert finder.findMedian() == -1
    finder.addNum(-2)
    assert finder.findMedian() == -1.5
    finder.addNum(-3)
    assert finder.findMedian() == -2
