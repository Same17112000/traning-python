
def makes_twenty(n1,n2):
    if n1 + n2 == 20:
        return True
    
    elif n1 == 20 or n2 == 20:
        return True
    else:
        return False
    
n1 = int(input())
n2 = int(input())

a = makes_twenty(n1,n2)
print(a)