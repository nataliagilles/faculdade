str1= input("Digite a primeira string:  ")
str2= input("Digite a segunda string:  ")
nova_str= ""

if str1 == "":
    print(str2)

if str2 == "":
    print(str1)

    
if len(str1) > len(str2):
    maior= len(str1)

else:
    maior= len(str2)
        
for i in range(maior):
    if i < len(str1):
            nova_str += str1[i]

    if i < len(str2):
            nova_str += str2[i]

print(nova_str)
