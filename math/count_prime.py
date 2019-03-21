#logic: find using the binary search nope
# another: simple count
# another: cna stakc the prime number and then divide by each

# learned: get an array and store the results so that from square ton in steps of that interger

def count_prime(n):
    if n < 3:
        return 0

    prime=[True]*n
    prime[0] = prime[1]=0

    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            prime[i*i:n:i] = [False]*len(prime[i*i:n:i])
    return sum(prime)

print(count_prime(10))