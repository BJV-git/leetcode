# logic: can split and then reverse words and then output

def reverse_III(s):
    return ' '.join([i[::-1] for i in s.split(' ') if i])

print(reverse_III("s'teL ekat edoCteeL tsetnoc"))
