def is_isogram(string:str):
    return not [c for c in string.lower() if string.lower().count(c) > 1 and c not in ["-", " "] ]
