class StringKeyDict(dict):
    def __setitem__(self, key, value):
        key = str(key)
        dict.__setitem__(self, key, value) # Why does this work?
# {1: 'A', '2': 'B', 3: 'C', '4': 'D'}

# dict1 =  StringKeyDict()
# dict1[1] = 'A'
# dict1[2] = 'B'
# print(dict1['1'])
# print(dict1['2'])

class RecentDict(dict):
    def __init__(self, max_length, **kwargs):
        self.max_length = max_length

    def __setitem__(self, key, value):
        dict.__setitem__(self, key, value)
        self.apply_max_length()

    def apply_max_length(self):
        if len(self) > self.max_length:
            item = list(self.keys())[0]
            del(self[item])

# dict2 = RecentDict(5)
# dict2[1] = 'A'
# dict2['2'] = 'B'
# dict2[3] = 'C'
# dict2['4'] = 'D'
# dict2[5] = 'E'
# print(dict2)
# dict2['6'] = 'F'
# print(dict2)
# dict2[7] = 'G'
# print(dict2)

class FlatList(list):

    def append(self, item):
        if iter(item):
            for n in item:
                list.append(n)

list1 = FlatList([1, 2, 3, 4, 5])
print(list1)
list1.append([6, 7, 8])
print(list1)
