# logic leanred: as its a limited range we knew that the max number of 1s can eb shown are 19 so jusyt use it

def isprime(L,R):
    return len([1 for i in range(L,R+1) if bin(i).count('1') in [2,3,5,7,11,13,17,19]])

print(bin(13268)[2:].count('1'))