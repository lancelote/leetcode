from src.implement_queue_using_stacks import MyQueue


def test_my_queue():
    mq = MyQueue()
    mq.push(1)
    mq.push(2)
    assert mq.peek() == 1
    assert mq.pop() == 1
    assert not mq.empty()
