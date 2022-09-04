from src.design_add_and_search_words_data_structure import WordDictionary


def test_word_dictionary():
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")

    assert not wd.search("pad")
    assert wd.search("bad")
    assert wd.search(".ad")
    assert wd.search("b..")
