"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    #...
    return result.replace("fooziman","f00z1m@n")  
r = fn_hack_5()
print(r)