# class FlexibleDict(dict):
#
#     def __getitem__(self, key):
#         try:
#             self[key]
#         except IndexError:
#             if self[int(key)]:
#                 return self[int(key)]
#             elif self[str(key)]:
#                 return self[str(key)]

class FlexibleDict(dict):
    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif str(key) in self:
                key = str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass
        return dict.__getitem__(self, key)

dict1 = FlexibleDict({1: 'A', '2': 'B', 3: 'C', '4': 'D'})

print(dict1[2])
