from sys import stdout
from HashMap import HashMap


class Node:

    def __init__(self, word):
        self.word = word
        self.parent_node = None
        self.child_nodes = HashMap(26*2+1)  # list of all the prefixes of this node (max 26 as the number of letters)
        self.line_numbers = HashMap(10)  # A list of all the numbers of lines in which the current word appears

    def reset_line_numbers(self):
        self.line_numbers = HashMap(10)

    @staticmethod
    def shared_prefix_len(a, b):  # finds the shared prefix for given 2 words
        min_len = min(len(a), len(b))
        for i in range(min_len):
            if a[i] != b[i]:
                return i
        return min_len

    def is_completed(self):  # if it's a word and not just a prefix
        return True if len(self.line_numbers) > 0 else False

    def search(self, word):  # search a word in the tree
        prefix_len = Node.shared_prefix_len(word, self.word)
        if prefix_len == len(word) and prefix_len == len(self.word):  # the same word
            return self
        elif prefix_len == len(self.word):  # same prefix
            char = word[prefix_len]
            if char in self.child_nodes:
                return self.child_nodes[char].lookup(word[prefix_len:])
        return None

    def lookup(self, word):
        prefix_len = Node.shared_prefix_len(word, self.word)
        if prefix_len == len(word) and prefix_len == len(self.word):  # same word
            return self
        elif prefix_len == len(word):  # the input word have shared prefix but the input word shorter the the exist word
            self.word = self.word[prefix_len:]  # suffix of exist word
            new_parent_node = Node(word[:prefix_len])  # the shared prefix
            # update child and parent
            new_parent_node.enter_child_node(self)
            new_parent_node.set_parent_node(self.parent_node)
            self.parent_node.enter_child_node(new_parent_node)
            self.set_parent_node(new_parent_node)
            return new_parent_node
        elif prefix_len == len(self.word):  # same length
            char = word[prefix_len]
            if char in self.child_nodes:  # if the prefix already exist
                return self.child_nodes[char].lookup(word[prefix_len:])  # lookup in the list of the current cell
            else:
                new_child_node = Node(word[prefix_len:])
                self.enter_child_node(new_child_node)
                new_child_node.set_parent_node(self)
                return new_child_node
        else:  # split current node for 2 suffixes (new and exist) and add to child list
            self.word = self.word[prefix_len:]  # 1 suffix
            # new parent
            new_parent_node = Node(word[:prefix_len])  # the shared prefix
            new_parent_node.set_parent_node(self.parent_node)  # parent for new parent - same parent
            self.parent_node.enter_child_node(new_parent_node)  # update different child for this parent
            # new child
            new_child_node = Node(word[prefix_len:])  # 2 suffix
            new_child_node.set_parent_node(new_parent_node)  # update the new parent for new child
            # update child for the new parent
            new_parent_node.enter_child_node(self)  # 1 suffix
            new_parent_node.enter_child_node(new_child_node)  # 2 suffix
            self.set_parent_node(new_parent_node)  # update the new parent for the 1 suffix
            return new_child_node

    def enter_line_number(self, line_number):
        self.line_numbers[line_number] = line_number

    def set_parent_node(self, parent_node):
        self.parent_node = parent_node

    def enter_child_node(self, child_node):
        self.child_nodes[child_node.word[0]] = child_node

    def remove_child_node(self, child_node):
        self.child_nodes.delete(child_node.word[0])

    def print(self, stack=""):
        if self.is_completed():
            print(f'{stack + self.word:10} -appears in the lines: {sorted(self.line_numbers.keys())}')
        for i, (char, node) in enumerate(sorted(self.child_nodes, key=lambda a: a[0])):
            node.print(stack + self.word)

    def print_for_tree(self, indent="", last=True, stack=""):
        stdout.write(indent)
        if last:
            stdout.write("┗╾ ")
            indent += "  "
        else:
            stdout.write("┣╾ ")
            indent += "┃ "
        if self.word == '':
            stdout.write('♣ROOT♣')
        else:
            stdout.write("{}".format(self.word))
        print(" {}".format(stack))
        for i, (char, node) in enumerate(sorted(self.child_nodes, key=lambda a: a[0])):
            node.print_for_tree(indent, i == len(self.child_nodes) - 1, stack)
