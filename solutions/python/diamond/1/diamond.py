def rows(c: str) -> list[str]:
    max_i = ord(c) - ord("A")

    def row(i: int) -> str:
        pad = " " * (max_i - i)
        letter = chr(ord("A") + i)
        if i == 0:
            return f"{pad}{letter}{pad}"
        inner = " " * (2 * i - 1)
        return f"{pad}{letter}{inner}{letter}{pad}"

    top = [row(i) for i in range(max_i + 1)]
    return top + top[-2::-1]  # include top then reversed top without middle
