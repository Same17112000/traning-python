a = "abddsbaxr"

def clear(a):
    valid = []
    invalid = []

    for i in a:
        if i not in valid and i not in invalid:
            valid.append(i)

        else:
            invalid.append(i)
            valid.pop(valid.index(i))
    
    return valid

b = clear(a)
b = "".join(b)
print(b)




