from src.design_browser_history import BrowserHistory


def test_solution():
    history = BrowserHistory("leetcode.com")
    history.visit("google.com")
    history.visit("facebook.com")
    history.visit("youtube.com")

    assert history.back(1) == "facebook.com"
    assert history.back(1) == "google.com"
    assert history.forward(1) == "facebook.com"

    history.visit("linkedin.com")

    assert history.forward(2) == "linkedin.com"
    assert history.back(2) == "google.com"
    assert history.back(7) == "leetcode.com"
