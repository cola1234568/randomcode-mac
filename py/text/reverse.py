def reverse(s: str):
    revarr = list(reversed(s))
    newstr = ''
    for i in revarr:
        newstr += i
    return newstr