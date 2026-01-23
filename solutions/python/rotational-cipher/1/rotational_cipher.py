from functools import partial

a, z, A, Z = ord("a"), ord("z"), ord("A"), ord("Z")

def rotate(text, key):
    return "".join(list(map(partial(shift, key), text)))

def shift(key: int, char: str) -> str:
    match ord(char):
        case c if (z >= c >= a): 
            if c + key > z: return chr(a + ((c-z-1) % key))
            return chr(c + key)
        case c if (Z >= c >= A):
            if c + key > Z: return chr(A + ((c-Z-1) % key))
            return chr(c + key)
        case _: return char 
