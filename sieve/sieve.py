def sieve(n):
    if n < 2:
        return []
    not_prime = set()
    prime = [2]
    for i in range(3, n+1, 2):
        if i not in not_prime:
            prime.append(i)
            not_prime.update(range(i*i, n, i))
    return prime
