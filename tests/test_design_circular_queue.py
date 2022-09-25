from src.design_circular_queue import MyCircularQueue


def test_solution_1():
    queue = MyCircularQueue(3)
    assert queue.enQueue(1) is True
    assert queue.enQueue(2) is True
    assert queue.enQueue(3) is True
    assert queue.enQueue(4) is False
    assert queue.Rear() == 3
    assert queue.isFull() is True
    assert queue.deQueue() is True
    assert queue.enQueue(4) is True
    assert queue.Rear() == 4
    assert queue.Front() == 2


def test_solution_2():
    queue = MyCircularQueue(6)
    assert queue.enQueue(6) is True
    assert queue.Rear() == 6
    assert queue.Rear() == 6
    assert queue.deQueue() is True
    assert queue.enQueue(5) is True
    assert queue.Rear() == 5
    assert queue.deQueue() is True
