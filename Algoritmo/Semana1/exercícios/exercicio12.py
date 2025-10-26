bolinha= 0

##posição das portas direita ou esquerda

direita= 1
esquerda= 0


portaP= int(input("A porta P está na direita'1' ou esquerda'0'?:  "))
portaR= int(input("A porta R está na direita'1' ou esquerda'0'?:  "))


if portaP==1 and portaR==1:
    print("A bolinha caiu no caminho A")

elif portaP==1 and portaR==0:
    print("A bolinha caiu no caminho B")

else:
    print("A bolinha caiu no caminho C")
    
