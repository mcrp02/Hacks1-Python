"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    i=0
    result = [1,2,3]
    lista = []
    for i in result:
        lista.append(i) 
        lista.append('@')
    return lista  

r = fn_hack_9()
print(r)