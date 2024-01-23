"""
loop: for [] output => [0,1,2,3,4,5]
"""

def fn_hack_6():
    ls = [0,1,2,3,4,5]
    lista = []
    for i in ls:
        if i < 6:
            lista.append(i)
    return lista
r = fn_hack_6()
print(r)