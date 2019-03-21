#logic: count the len and make the decisions

def text_justification(words, maxWidth):
    temp=''
    # curr=''
    result=[]

    for i in words:
        curr=i
        new =  temp + curr
        temp_len= len(new)

        if temp_len == maxWidth:
            result.append(new)
            temp=''
        elif temp_len < maxWidth:
            temp = new + ' '
        else:
            l = sum(j.isalpha() for j in temp)
            sp=temp.split(' ')[:-1]
            sl = len(sp)

            remain , extra= (maxWidth-l)//(sl-1),  (maxWidth-l)%(sl-1)

            if sl==1:
                result.append(sp[0]+' '*remain)
            elif extra ==0: # means that we include equally
                space=' '*remain
                result.append(space.join(sp))
            elif extra >0:
                space = ' ' * remain
                result.append( sp[0]+ ' '*(remain+extra) + space.join(sp[1:]))
            # else:
    if result[-1]


print('hi b '.split(' ')[:-1])