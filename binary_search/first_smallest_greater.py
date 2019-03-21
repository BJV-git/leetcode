# logic: just use % for gettign first, as we need ot output only the given ones


def first(letters,target):
    for i in letters:
        if i > target:
            return i
    return letters[0]

print(first(['c','f','j'],'k'))