# logic: consider each letter

def rotate_num(n):
    count=0
    dic = {'0':'0','1': '1', '2': '5', '5': '2', '6': '9', '8': '8', '9': '6'}
    while n >1:
        org = str(n)
        rot=''

        if '3' in org or '4' in org or '7' in org:
            n-=1
            continue


        for i in org:
            rot = rot+dic[i]

        if org!=rot:
            count+=1

        n-=1
    return count
print(rotate_num(3))
