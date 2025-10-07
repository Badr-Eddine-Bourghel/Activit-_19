def F7(n):
    if n<2:
        return 1
    else:
        return F7(n-1)+F7(n-2)
for i in range(5):
    if i < 2:
        print(f"F7({i})={F7(i)}")
    else:
        print(f"F7({i})=F7({i-2})+F7({i-1})={F7(i-2)}+{F7(i-1)}={F7(i)}")
"""
def F1(n):
    print("Bonjour\n"*n)
F1(int(input("n = ")))

def F2(n):
    if n%10==0:
        print(f"{n} est divisible par 10")
    else:
        print(f"{n} n'est pas divisible par 10")

F2(int(input("veuillez saisir un entier n : ")))
print()

def F3(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(f"n!={fact}")
F3(int(input("Veuillez saisir un nombre entier : ")))
print()

def F4(chaine):
    voyelles=['a','e','i','o','u']
    num_voyelles=0
    for char in chaine:
        if char in voyelles:
            num_voyelles+=1
    print(f"le nombres de voyelles dans cette chaine est : {num_voyelles}")
F4(input("Veuillez saisir une chaine de caractéres : "))

def F5(n):
    for i in range(1,10):
        print(f"{n}*{i}={n*i}")
F5(int(input("Veuillez saisir un entier : ")))

def F6(mot):
    num_caratéres = 0
    for char in mot : 
        num_caratéres+=1
    print(f"ce est composé de {num_caratéres} caractéres")
F6(input("veuillez saisr un mot : "))
"""