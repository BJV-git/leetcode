


def findwords(words):
    res=[]

    key_board = {1:set(['a','s','d','f','g','h','j','k','l']), 0: set(['q','w','e','r','t','y','u','i','o','p']),
                 2:set(['z','x','c','v','b','n','m'])}
    for word in words:
        l = set(list(word.lower()))
        if l <= key_board[0] or  l<=key_board[1] or l <= key_board[2]:
            res.append(word)

    return res

print(findwords(["Hello", "Alaska", "Dad", "Peace"]))
