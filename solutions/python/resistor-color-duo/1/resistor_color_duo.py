def value(colors):
    d1, d2, *_ = map(lambda color: r_code.get(color, -1), colors)
    return 10*d1 + d2

r_code = {"black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4, "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9}