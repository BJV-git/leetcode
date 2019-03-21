# logic: So return the last + reverse + first

def recur_reverse_str(s):
    if len(s)==1:
        return s

    return s[-1] + recur_reverse_str(s[1:-1]) + s[0]

print(recur_reverse_str('sonam'))

