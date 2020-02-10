#l = [1, 2, 3, 4, 5]
l = list(range(1000000))

while True:
    left = int(input())
    right = int(input())
    counter = 0
    for i in l[left:right]:
        counter += i
    print(counter)
    break
