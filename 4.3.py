
def check_valid(s: str):
    if len(s) < 5:
        return False

    if not s.isalnum() or not s.islower():
        return False

    letter_count = len([i for i in s if i.isalpha()])
    if not letter_count % 2:
        return False

    num_count = len([i for i in s if i.isdigit()])
    if num_count % 2:
        return False

    return True


print(check_valid("rrrrrr"))
print(check_valid("R22rtyt"))
print(check_valid("r22rtyt"))
print(check_valid("r223rtyt"))
print(check_valid("r22rtyt!"))
print(check_valid("r22"))



