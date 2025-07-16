def swap_case(s):
    res = ''
    for i in range(len(s)):
        if s[i].islower():
            res  += s[i].upper()
        elif s[i].isupper():
            res += s[i].lower()
        else:
            res += s[i]

    return res


