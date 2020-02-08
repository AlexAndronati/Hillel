
def swap (target_list, item_index1, item_index2):
    target_list[item_index1], target_list[item_index2] = target_list[item_index2], target_list[item_index1]


l = [1, 2, [6, 8], 4, 5, 6]
print("Initial list: ", l)
index1 = int(input("Enter first index: "))
index2 = int(input("Enter first index: "))
swap(l, index1, index2)
print("New list: ", l)
