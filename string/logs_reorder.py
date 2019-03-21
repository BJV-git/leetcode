

def loges_reorder(logs):
    digit=[]
    letter=[]

    for i in logs:
        if i.split(' ')[1].isalpha():
            print(i.split(' ')[0])
            letter.append(i)
        else:
            digit.append(i)

    letter.sort(key = lambda x: (x.split(' ')[1],x.split(' ')[1:]))
    print(letter)
    print(digit)
    return letter + digit

print(loges_reorder(["qi ir oo i", "cp vnzw i", "0 fkbikbts", "4 j trouka", "gn j q al", "5r w wgqc", "m8 x haje", "fg 28694 6", "i gf mwdoa", "ao 0850716"]))

# ['0 fkbikbts', 'i gf mwdoa', 'qi ir oo i', '4 j trouka', 'gn j q al', 'cp vnzw i', '5r w wgqc', 'm8 x haje', 'fg 28694 6', 'ao 0850716']
# ["0 fkbikbts","i gf mwdoa","qi ir oo i","gn j q al","4 j trouka","cp vnzw i","5r w wgqc","m8 x haje","fg 28694 6","ao 0850716"]