"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    i=6
    lista = []
    while i >= 1:
        i= i-1
        if i < 6:
            lista.append(i)
    return lista      
r= fn_hack_7()
print(r)
