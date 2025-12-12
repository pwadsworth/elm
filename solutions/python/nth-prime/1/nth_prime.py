from math import isqrt


def prime(n: int) -> int:
    """Return the nth prime number (1-indexed).

    :param n: positive integer index (1 -> 2, 2 -> 3, ...)
    :return: the nth prime as an int
    :raises ValueError: if n < 1
    """
    if n < 1:
        raise ValueError('there is no zeroth prime')

    primes = []
    candidate = 2

    while len(primes) < n:
        if _is_prime(candidate, primes):
            primes.append(candidate)
        candidate += 1 if candidate == 2 else 2  
    return primes[-1]


def _is_prime(value: int, primes: list[int]) -> bool:
    if value < 2:
        return False
    limit = isqrt(value)
    for p in primes:
        if p > limit:
            break
        if value % p == 0:
            return False
    return True
