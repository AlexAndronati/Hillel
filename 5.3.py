

def type_counter(l: list):
    types_dict = {}
    for i in l:
        if str(type(i)) not in types_dict:
            types_dict[str(type(i))] = 1
        else:
            types_dict[str(type(i))] += 1
    return types_dict


list1 = [1, 'one', 'two', 3.0, 4j, 5j, 3, 2, 12., 17, [1, 2], {1: 1}]
print(*type_counter(list1).items(), sep='\n')