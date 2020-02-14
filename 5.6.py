
def adder(l, left, right):

    counter = 0
    for i in l[left:right]:
        counter += i
    return counter


l = range(100_000_000)

left = int(input("Enter the left border: "))
right = int(input("Enter the right border: "))

print(adder(l, left, right))
