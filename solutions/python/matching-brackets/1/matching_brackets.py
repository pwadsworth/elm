def is_paired(input:str):
    acc, map= [], {'[':']', '(':')', '{':'}'}
    for ch in input:
        if ch in map.keys():
            acc.append(ch)
        if ch in map.values() and (acc == [] or map[acc.pop()] != ch):
            return False
    return acc == []