def input_int(n,m):
    suma=int(n)+int(m)
    return suma

def input_int(n,m):
    suma=float(n)+float(m)
    return suma

def input_int(n,m):
    suma=bool(n)+bool(m)
    return suma



v=input("Enter the type of number:")

if v=="integer":
    n=input("enter first integer")
    m=input("enter second integer")
    suma=input_int(n,m)
    print(suma)

elif v=="float":
    n=input("enter first float")
    m=input("enter second float")
    suma=input_int(n,m)
    print(suma)

elif v=="boolean":
    n=input("enter first boolean")
    m=input("enter second boolean")
    suma=input_int(n,m)
    print(suma)
