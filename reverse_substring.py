def rev_substring(stri, startindex, endindex):
    i = len(stri) - 1
    newstr = ''
    while i >= 0:
        if i > endindex:
            i -= 1
            continue
        if i < startindex:
            break
        newstr += (stri[i])
        i -= 1
    return newstr

stri = "Hi How are you"

print(rev_substring(stri, 3, 5))
