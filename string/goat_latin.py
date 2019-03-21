

def togoatlatin(s):
    s=[i for i in s.strip().split(' ') if i]
    slen=len(s)

    for i in range(slen):
        if s[i][0].lower() in ['a','e','i','o','u']:
            s[i]+= 'ma'
        else:
            s[i] = s[i][1:] + s[i][0] +'ma'

        s[i] = s[i]+'a'*(i+1)

    return ' '.join(s)

print(togoatlatin("I speak Goat Latin"))