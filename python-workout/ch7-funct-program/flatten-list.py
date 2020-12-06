def flatten(lists):
    return [num for sublist in lists for num in sublist]

print(flatten([[1, 2], [3, 4]]))

def flatted_odd_ints(lists):
    return [num for sublist in lists for num in sublist if str(num).isdigit() if int(num) % 2 != 0]

print(flatted_odd_ints([[1, '2', '3','b', 7, '4'], ['a', 'b', '5', 6, '7']]))

family = {'A':['B', 'C', 'D'], 'E':['F', 'G']}

def grandkids(dict):
    return [grankid for items in dict.keys() for grankid in dict[items]]

print(grandkids(family))

family = {'A':['B': {'Fer', 15}, 'C': {'Laura', 34}, 'D': {'Pao', 24}], 'E':['F': {'Tanaka', 14}, 'G': {'Yi', 20}]}

def grandkids2(dict):
    return
