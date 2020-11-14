from Node import Node


class RadixTree:
    def __init__(self):
        self.root = Node('')

    def get(self, word, create_if_not_found=True):
        if create_if_not_found:
            return self.root.lookup(word)  # lookup suitable node to update
        else:
            return self.root.search(word)  # search a word

    def insert(self, word, line_number):
        node = self.get(word, create_if_not_found=True)
        node.enter_line_number(line_number)

    def find(self, word):
        node = self.get(word, create_if_not_found=False)
        return sorted(node.line_numbers.keys()) if node is not None and node.is_completed() else None

    def remove(self, word):
        node = self.get(word, create_if_not_found=False)
        if node is None or not node.is_completed():
            return False
        else:
            node.reset_line_numbers()

            return True

    def insert_words_from_file(self, file_name):
        with open(file_name, 'r') as input_file:
            count_lines = 1
            for line in input_file:
                for word in line.split(' '):
                    if word[-1] == '\n':
                        word = word[:-1]
                    if word != "":
                        self.insert(word.lower(), count_lines)
                count_lines += 1

    def print(self):
        print('Alphabetical List:')
        self.root.print()

    def print_for_tree(self):
        print('\n**/\\** RADIX TREE **/\\**\n')
        self.root.print_for_tree()
