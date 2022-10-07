from src.my_calendar_iii import MyCalendarThree


def test_solution():
    cal = MyCalendarThree()
    assert cal.book(10, 20) == 1
    assert cal.book(50, 60) == 1
    assert cal.book(10, 40) == 2
    assert cal.book(5, 15) == 3
    assert cal.book(5, 10) == 3
    assert cal.book(25, 55) == 3
