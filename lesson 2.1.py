
s = "spam and eggs or eggs with spam"
set_of_letters = set()
for i in s:
    if i not in set_of_letters:
        print(f"\'{i}\':{s.count(i)}")
    set_of_letters.update(i)

