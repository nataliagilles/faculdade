A= float(input("Digite o primeiro valor(A):  "))
B= float(input("Digite o segundo valor(B):  "))
C= float(input("Digite o terceiro valor(C):  "))

if A > B:
    A,B= B,A

if A > C:
    A,C= C, A

if B > C:
    B,C= C, B

print(f"Os valores {A}, {B} e {C} em ordem crescente é:\n A= {A},\n B= {B}, \n C= {C}")
