# logic: basically need to count and make sure we can

def canconstruct(ransomNote, magazine):
    ref={}
    for i in magazine:

        ref[i] = ref.get(i,0)+1
    for j in ransomNote:

        ref[j]=ref.get(j,0)-1
        if ref[j] <0:
            return False
    return True
print(canconstruct("hi bujji", "biijjhu"))