# logic: compare simply

# better to append zero to compare when the try gives error, so instead anyways its gonna be 1 so lets just keep 1 over there in
# comparision


def version_compare(v1,v2):
    changed=0
    if v1==v2:
        return 0

    v1 = v1.split('.')
    v2 = v2.split('.')

    v1len = len(v1)
    v2len= len(v2)


    if v2len < v1len:
        v1,v2 = v2,v1
        v1len,v2len = v2len, v1len
        changed=1

    print(v1)


    for i in range(v2len):
        print("i",i)
        try:
            if int(v1[i]) > int(v2[i]):
                if changed==1:
                    return -1
                else:
                    return 1
        except:
            pass

        try:
            if int(v1[i]) < int(v2[i]):

                if changed==1:
                    return 1
                else:
                    return -1
        except:
            print("reached for i",i)
            if 0 < int(v2[i]):
                if changed==1:
                    return 1
                else:
                    return -1

    return 0




print(version_compare('1.1', '1'))


