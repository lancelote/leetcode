from src.implement_stack_using_queues import MyStack


def test_solution():
    my_stack = MyStack()
    my_stack.push(1)
    my_stack.push(2)

    assert my_stack.top() == 2
    assert my_stack.pop() == 2
    assert not my_stack.empty()
    assert my_stack.top() == 1
    assert my_stack.pop() == 1
    assert my_stack.empty()
