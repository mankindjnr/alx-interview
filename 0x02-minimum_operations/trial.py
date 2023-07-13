def isPrime(number):
    if number < 2:
        return False
    
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def primes(n):
    prime_factors = []
    div = 2

    if not isinstance(n, int) or n <= 1:
        return 0

    if n == 1:
        return 1

    
    while True:
        if n % div == 0:
            prime_factors.append(div)
            n = int(n/div)
        else:
            while True:
                div += 1
                if (isPrime(div)):
                    break
        
        if n == 1:
            break
    
    print(prime_factors)

    minOps = sum([prime for prime in prime_factors])
    return(minOps)

print(primes(12))  

