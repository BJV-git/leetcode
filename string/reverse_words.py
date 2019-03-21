# logic: split adn strip and read from reverse

def reverse_words(s):

    s = s.split(' ')
    slen=len(s)
    # print(slen)

    if slen==1:
        return s[0]
    opt=''
    for i in range(slen-1,-1,-1):
        if s[i].strip(' '):
            opt= opt + s[i]+ ' '
    return(opt.rstrip(' '))



print(reverse_words('hello world!'))