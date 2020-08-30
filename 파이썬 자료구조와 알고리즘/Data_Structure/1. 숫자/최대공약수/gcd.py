def gdc(a,b):
    while(b!=0):
        result=b
        a, b = b, a % b
    return result

print(gdc(100,64))