
def find_median(l: list):
    l.sort()
    if len(l) % 2 == 1:
        return l[(len(l))//2]
    else:
        return (l[(len(l))//2]+l[(len(l))//2-1])/2


list1 = [1, 2, 4, 7, -5,7,7]
print(list1)
print(sorted(list1))
print(find_median(list1))

list2 = [1, 2, 4, 7, -5, 12]
print(list2)
print(sorted(list2))
print(find_median(list2))
