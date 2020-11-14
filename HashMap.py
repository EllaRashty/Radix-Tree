class HashMap(object):
    def __init__(self, length=26):
        self.table = [None] * length
        self.length = 0

    def hash(self, key):  # convert key into an array index
        length = len(self.table)
        return hash(key) % length

    def update(self, key, value):  # add or update
        i = self.hash(key)  # get the key after convert
        if self.table[i] is not None:  # if the cell isn't empty
            for pair in self.table[i]:  # checks if the key is already existing
                if pair[0] == key:
                    pair[1] = value  # if it's already existing update the value
                    return
        else:
            self.table[i] = []
        self.table[i].append([key, value])
        self.length += 1
        if self.is_full():
            self.double()

    def get(self, key, default_value=None):
        i = self.hash(key)  # get the key after convert
        if self.table[i] is None:  # if the cell is empty
            if default_value:
                return default_value
            raise KeyError()
        else:
            for k, v in self.table[i]:
                if k == key:
                    return v
            if default_value:
                return default_value
            raise KeyError()

    def keys(self):
        keys = []
        for k, v in self.__iter__():
            keys.append(k)
        return keys

    def values(self):
        values = []
        for k, v in self.__iter__():
            values.append(v)
        return values

    def items(self):
        items = []
        for pair in self.__iter__():
            items.append(pair)
        return items

    def is_full(self):
        return self.length > len(self.table) / 2

    def double(self):  # increases the HashMap size
        new_hash_map = HashMap(len(self.table) * 2)
        for k, v in self.__iter__():
            new_hash_map.update(k, v)
        self.table = new_hash_map.table

    def pop(self, key, default_value=None):
        i = self.hash(key)  # get the key after convert
        if self.table[i] is None:  # if the cell is empty
            if default_value:
                return default_value
            raise KeyError()
        else:
            for j, (k, v) in enumerate(self.table[i]):
                if k == key:
                    del self.table[i][j]
                    self.length -= 1
                    return v
            if default_value:
                return default_value
            raise KeyError()

    def delete(self, key):
        try:
            self.pop(key)
            return True
        except KeyError:
            return False

    def clear(self):
        self.table = HashMap().table
        self.length = 0

    def __len__(self):
        return self.length

    def __iter__(self):
        for pairs in self.table:
            if pairs is None:
                continue
            for k, v in pairs:
                yield (k, v)

    def __str__(self):
        string = ''
        string += '{'
        first = True
        for k, v in self.__iter__():
            if not first:
                string += ', '
            else:
                first = False
            string += f'{k}: {v}'
        string += '}'
        return string

    def __contains__(self, key):
        try:
            self.get(key)
            return True
        except KeyError:
            return False

    def __setitem__(self, key, value):
        self.update(key, value)

    def __getitem__(self, key):
        return self.get(key)
