class TrieNode:
    def __init__(self, char: str):
        self.char = char
        self.count = 1
        self.children = []
        self.last_word = False


def add(root, word: str):
    node = root
    for char in word:
        found_in_child = False

        for child in node.children:
            if char == child:
                child.count += 1
                node = child
                found_in_child = True
                break

        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node)
            node = new_node
    node.last_word = True


if __name__ == "__main__":
    root = TrieNode('*')
    add(root,'apple')
    add(root,'apples')