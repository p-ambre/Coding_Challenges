def substring(stri, startindex, endindex):
    i = 0
    newstr = ''
    while i < len(stri):
        if i < startindex:
            i += 1
            continue
        if i > endindex:
            break
        newstr += stri[i]
        i += 1
    return newstr

def reverse(stri):
    j = len(stri) - 1
    newstr1 = ''
    while j >= 0:
        newstr1 += (stri[j])
        j -= 1
    return newstr1

stri = "Hi How are you"

print(substring(stri, 3, 5))
print(reverse(substring(stri, 3, 5)))
print(reverse(stri))
