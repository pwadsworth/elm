def label(colors: list[str]):
    d1, d2, zeros, *_ = map(lambda color: r_code.get(color, -1), colors)
    r = (10*d1 + d2) * 10**zeros
    return f"{to_metric(r)}ohms"

def to_metric(n:int) -> str:
    if n >= 10**9:
        return f"{int(n/10**9)} giga"
    if n >= 10**6:
        return f"{int(n/10**6)} mega"
    if n >= 10**3:
        return f"{int(n/10**3)} kilo"
    else:
        return f"{n} "
 
r_code = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}