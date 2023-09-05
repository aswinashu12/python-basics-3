x=int(input("enter a number from 0-4: 1:add 2:sub 3:mul: 4:div"))

def sum(n1, n2):
    add = n1 + n2
    return add

def sub(n1, n2):
    diff = n1 - n2
    return diff

def mul(n1, n2):
    mult = n1 * n2
    return mult

def div(n1,n2):
    divs=n1/n2
    return divs
def calc(n1,n2):
    if x==1:
        return sum(n1,n2)
    elif x==2:
        return sub(n1,n2)
    elif x==3:
        return mul(n1,n2)
    elif x==4:
        return div(n1,n2)
    else:
        print("invalid")
