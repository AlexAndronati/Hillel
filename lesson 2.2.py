
a = [1, 3, 4, 5, 8, 10, 15, 16, 23, 56, 127]

n = int(input())
left = 0
right = len(a)-1
center = (left+right)//2

while left <= right:
    if n == a[center]:
        print("Элемент найден! Его индекс = ", center)
        break
    elif n < a[center]:
        right = center-1
    else:
        left = center+1

    center = (right + left) // 2
else:
    print("Элемент не найден")
