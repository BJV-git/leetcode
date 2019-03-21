def get_zig_zag(str,rows):
    opt = [[] for i in range(rows)]
    len_str= len(str)
    i=0

    if len_str <= rows:
        return str

    while i < len_str:
        for j in range(rows):
            if i < len_str:

                opt[j].append(str[i])
                i+=1
            else:
                return ''.join([''.join(i) for i in (opt)])

        if rows > 2:

            for z in range(rows-2,0,-1):
                if i < len_str:
                    opt[z].append(str[i])
                    i+=1
                else:
                    return ''.join([''.join(i) for i in (opt)])

    return ''.join([''.join(i) for i in (opt)])


print(get_zig_zag('ABCDE',4))
#
# for i in range(5,1,-1):
#     print(i)