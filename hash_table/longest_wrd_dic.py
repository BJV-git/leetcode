# logic: should start from letter one length
# sort the stuff and then see where it gonna break


def longestwrd(words):
    words.sort()

    words_set, longest_word = set(['']), ''
    for word in words:
        if word[:-1] in words_set:
            words_set.add(word)
            if len(word) > len(longest_word):
                longest_word=word
    return longest_word

    res=[]
    temp=""
    maxi=0
    for i in words:
        if len(i)==1:
            maxi = max(maxi, len(temp))
            res.append(temp) # till then the max one lexi small one
            temp = i
        elif temp and temp in i:
            temp =i
        elif temp and temp[:-1] in i:
            temp = min(temp,i)

    res.append(temp)
    maxi = max(maxi, len(temp))
    res=[i for i in res if len(i)==maxi]
    print(res)
    l=res[-1][0]
    if not res:return ""
    # return the min in the highest
    print(min([i for i in res if i[0]==l]))

# print(sorted(["a", "banana", "app", "appl", "ap", "apply", "apple", "b","ba", "ban","bana", "banan","banana"]))
print(longestwrd(["m","mo","moc","moch","mocha","l","la","lat","latt","latte","c","ca","cat"]))