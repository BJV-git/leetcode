

def uniq_mails(arr):
    arr=[i[:i.find('@')].replace('.','')+i[i.find('@'):] for i in arr]
    arr=[ i[:i.find('+')]+i[i.find('@'):] if '+' in i else i for i in arr]
    print(arr)
    print(len(set(arr)))

print(uniq_mails(["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]))
# a="test.email+alex@leetcode.com"
# print(a[:10]+a[15:])
