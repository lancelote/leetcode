from src.design_linked_list import MyLinkedList


def test_my_linked_list():
    my_list = MyLinkedList()
    my_list.addAtHead(1)
    my_list.addAtTail(3)
    my_list.addAtIndex(1, 2)

    assert my_list.get(1) == 2

    my_list.deleteAtIndex(1)

    assert my_list.get(1) == 3
    assert my_list.get(2) == -1


def test_delete_0():
    my_list = MyLinkedList()
    my_list.addAtHead(1)
    my_list.deleteAtIndex(0)

    assert my_list.get(0) == -1


def test_get_0():
    my_list = MyLinkedList()
    my_list.addAtIndex(0, 10)
    my_list.addAtIndex(0, 20)
    my_list.addAtIndex(0, 30)

    assert my_list.get(0) == 30
    assert my_list.get(3) == -1


def test_get_non_existent():
    my_list = MyLinkedList()

    assert my_list.get(0) == -1
    assert my_list.get(1) == -1

    my_list.addAtIndex(0, 1)

    assert my_list.get(0) == 1
    assert my_list.get(1) == -1
    assert my_list.get(2) == -1


def test_add_at_tail():
    my_list = MyLinkedList()
    my_list.addAtTail(1)
    my_list.addAtTail(2)

    assert my_list.get(0) == 1
    assert my_list.get(1) == 2
    assert my_list.get(2) == -1


def test_delete_unknown_index():
    my_list = MyLinkedList()
    my_list.addAtTail(1)
    my_list.addAtTail(2)
    my_list.deleteAtIndex(5)

    assert my_list.get(0) == 1
    assert my_list.get(1) == 2
    assert my_list.get(2) == -1


def test_add_at_unknown_index():
    my_list = MyLinkedList()
    my_list.addAtHead(2)
    my_list.addAtHead(1)
    my_list.addAtIndex(5, 3)

    assert my_list.get(0) == 1
    assert my_list.get(1) == 2
    assert my_list.get(2) == -1


def test_add_at_last_index():
    my_list = MyLinkedList()
    my_list.addAtHead(1)
    my_list.addAtIndex(1, 2)

    assert my_list.get(0) == 1
    assert my_list.get(1) == 2
    assert my_list.get(2) == -1
