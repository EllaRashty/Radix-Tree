from Tree import RadixTree

if __name__ == "__main__":

    tree = RadixTree()
    op = ''


    while op != '5':
        print(
            '\n1 - Insert words from file \n2 - Find word \n3 - Delete word \n4 - Print list \n5 - Exit \n6 - Print RADIX Tree')
        op = input('Choose an option: ')

        if op == '1':
            name_of_file = input('Type name of file: ')
            tree.insert_words_from_file(name_of_file)
            tree.print()
        elif op == '2':
            word = input('Type a word: ')
            lines = tree.find(word.lower())
            if lines is None:
                print(f'Did not found word `{word}`')
            else:
                print(f'Found word `{word}` in lines {lines}')
        elif op == '3':
            word = input('Type a word: ')
            is_removed = tree.remove(word.lower())
            if not is_removed:
                print(f'Did not found word `{word}`')
            else:
                print(f'Removed word `{word}`')
        elif op == '4':
            tree.print()
        elif op == '5':
            print('Exiting...')
        elif op == '6':
            tree.print_for_tree()
        else:
            print('Wrong option...\n')
