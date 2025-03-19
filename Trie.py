from typing import List


class TrieNode:
    def __init__(self):
        self.children: List[TrieNode] = [None] * 26
        self.end_of_word = False


class Trie:
    """
    A Trie (prefix tree) implementation for storing and searching strings.

    Methods
    -------
    __init__():
        Initializes the Trie with an empty root node.

    insert(word: List[str]):
        Inserts a word into the Trie.
        Time Complexity: O(n), where n is the length of the word.
        Space Complexity: O(n), where n is the length of the word.

    get_all_words(root_node: TrieNode) -> List[str]:
        Retrieves all words stored in the Trie starting from the given root node.
        Time Complexity: O(m), where m is the total number of nodes in the Trie.
        Space Complexity: O(m), where m is the total number of nodes in the Trie.

    search(word: List[str]) -> bool:
        Searches for a word in the Trie.
        Time Complexity: O(n), where n is the length of the word.
        Space Complexity: O(1).

    starts_with(prefix: str) -> bool:
        Checks if there is any word in the Trie that starts with the given prefix.
        Time Complexity: O(p), where p is the length of the prefix.
        Space Complexity: O(1).

    get_all_words_with_prefix(prefix: str) -> List[str]:
        Retrieves all words in the Trie that start with the given prefix.
        Time Complexity: O(p + m), where p is the length of the prefix and m is the number of nodes in the sub-trie.
        Space Complexity: O(m), where m is the number of nodes in the sub-trie.
    """

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: List[str]):
        current = self.root
        for char in word:
            index = ord(char) - ord("a")
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.end_of_word = True

    def get_all_words(self, root_node: TrieNode) -> List[str]:
        all_words = []

        def dfs(root_node: TrieNode, current_word: str = ""):
            if root_node is None:
                return
            if root_node.end_of_word:
                all_words.append(current_word)

            for indx, children in enumerate(root_node.children):
                if children is not None:
                    word = current_word + chr(indx + ord("a"))
                    dfs(root_node=children, current_word=word)

        dfs(root_node=root_node)
        return all_words

    def search(self, word: List[str]):
        if not word:
            return False
        current = self.root
        for char in word:
            index = ord(char) - ord("a")
            if current.children[index] is not None:
                current = current.children[index]
                continue
            return False
        return current.end_of_word

    def starts_with(self, prefix: str):
        if not prefix:
            return False
        current = self.root
        for char in prefix:
            index = ord(char) - ord("a")
            if current.children[index]:
                current = current.children[index]
                continue
            return False
        return True

    def get_all_words_with_prefix(self, prefix: str) -> List[str]:
        all_words = []

        current = self.root
        for char in prefix:
            index = ord(char) - ord("a")
            if current.children[index]:
                current = current.children[index]
                continue
            return all_words
        root_node = current
        all_words = self.get_all_words(root_node=root_node)
        return [prefix + word for word in all_words]


def main():
    words_to_insert = ["apple", "apply", "appex"]

    trie_obj = Trie()

    for word in words_to_insert:
        trie_obj.insert(word=word)

    assert trie_obj.search(word="apply") == True
    assert trie_obj.search(word="app") == False
    assert trie_obj.starts_with(prefix="app") == True
    assert trie_obj.starts_with(prefix="pp") == False
    assert set(trie_obj.get_all_words(root_node=trie_obj.root)) == set(words_to_insert)
    assert set(trie_obj.get_all_words_with_prefix(prefix="appl")) == set(
        ["apple", "apply"]
    )


if __name__ == "__main__":
    main()
