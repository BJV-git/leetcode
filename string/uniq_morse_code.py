# just make the transformation and return uniq num

import string

def morse_code_uniq(words):

    cont= [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    al = list(string.ascii_lowercase)

    dic = dict(zip(al,cont))

    a = set()

    for i in words:
        change=''
        for j in i:
            change+=dic[j]
        a.add(change)

    return len(a)

print(morse_code_uniq(["g", "z", "g", "m"]))