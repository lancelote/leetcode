import pytest

from src.reconstruct_itinerary import Solution


@pytest.mark.parametrize(
    "tickets,expected",
    (
        (
            [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]],
            ["JFK", "MUC", "LHR", "SFO", "SJC"],
        ),
        (
            [
                ["JFK", "SFO"],
                ["JFK", "ATL"],
                ["SFO", "ATL"],
                ["ATL", "JFK"],
                ["ATL", "SFO"],
            ],
            ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"],
        ),
        (
            [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]],
            ["JFK", "NRT", "JFK", "KUL"],
        ),
    ),
)
def test_solution(tickets, expected):
    assert Solution().findItinerary(tickets) == expected
