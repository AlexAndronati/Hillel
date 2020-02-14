
def capitals(s: str):
    return "".join(i for i in s if i.isupper())


st = "Help ELephant learn LOops. While's and fOrs. RLD!"
print(st)
print(capitals(st))
