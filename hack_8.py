"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1,3,5,7,9]
    lista=[]
    for i in result:
        if i > 2 and i < 8:
            lista.append(i)
    return lista

r = fn_hack_8()
print(r)