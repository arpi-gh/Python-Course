# class Hashtable:
#     def __init__(self):
#         self.__hash_table = []
#         self.__current_index = len(self.__hash_table)
#
#     def add_item(self, item: tuple):
#         if type(item) is tuple:
#             self.__hash_table[self.__current_index] = item
#         else:
#             raise ValueError('Keys and values need to be grouped in a tuple. ')


class ImmutableMap:
    def __init__(self, keys: list, values: list):
        self.keys = keys
        self.values = values
        self.__items = dict(zip(self.keys, self.values))
        self.__index = 0

    @property
    def keys(self):
        return self.__keys

    @keys.setter
    def keys(self, k):
        if hasattr(self, '_ImmutableMap__keys'):   # Thank you, ChatGPT for this line
            raise TypeError("Can't add/remove/change keys after initialization")
        elif not isinstance(k, list):
            raise ValueError
        else:
            self.__keys = k

    @property
    def values(self):
        return self.__values

    @values.setter
    def values(self, v):
        if hasattr(self, '_ImmutableMap__values'):
            raise TypeError("Can't add/remove/change values after initialization")
        elif not isinstance(v, list):
            raise ValueError
        else:
            self.__values = v
            if len(self.__values) != len(self.__keys):
                raise ValueError('The number of keys must correspond to the number of values.')

    @property
    def items(self):
        return self.__items

    def __len__(self) -> int:
        return len(self.__items)

    def __iter__(self) -> None:
        return self

    def __next__(self):
        if self.__index < len(self.__items):
            next_elem = self.__items[self.__index]
            self.__index += 1
            return next_elem
        else:
            raise StopIteration

    def __setitem__(self, key, value):
        raise TypeError("Can't add/remove/change items after initialization.")

    def __getitem__(self, key):
        return self.__items[key]

    def __contains__(self, key) -> bool:
        return key in self.keys

    def __repr__(self):
        return f'{self.__items}'


if __name__ == '__main__':
    my_map = ImmutableMap(['key1', 'key2', 'key3'], [1, 2, 3])
    print('Items: ', my_map.items)
    print('Keys: ', my_map.keys)
    print('Values: ', my_map.values)
    print('Length: ', len(my_map))
    # my_map['key1'] = 4  # This should result in an error
    # my_map.keys = [1, 2, 3] # This should result in an error
    x = 'key1' in my_map
    print('Contains key1: ', x)
    print(my_map)
    for key in my_map.keys:
        print(key)
    for val in my_map.values:
        print(val)
