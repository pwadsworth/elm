def steps(n):
    acc = 0
    if n <= 0: 
        raise ValueError("Only positive integers are allowed")
    while n > 1:
        if n%2 == 0:
            acc += 1
            n = n / 2
        else: 
            acc += 1
            n = n * 3 + 1
    return acc
