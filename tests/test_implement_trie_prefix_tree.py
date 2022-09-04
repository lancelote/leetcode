from src.implement_trie_prefix_tree import Trie


def test_trie():
    trie = Trie()
    trie.insert("apple")

    assert trie.search("apple")
    assert not trie.search("app")
    assert trie.startsWith("app")

    trie.insert("app")

    assert trie.search("app")
