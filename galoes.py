#!/usr/bin/env python3

# compra apenas com galões 
#calcular o preço e a quantidade de galoes pra comprar 
#saber a area do cliente 
area=int(input("qual a area a ser pintada "))
#calcular a quantidade de tinta (area /6)
litros_tinta=area/6
#calcular a quantidade de galões e arredondar pra cima litros /3,6
#verifico se a quantidade de galões vai ser uma divisão inteira 
#caso não seja 
#galões vai ser a parte inteira da divisão +1
#caso seja 
#galões vai ser a divisão de litros por 3,6
galoes=litros_tinta/3.6
if litros_tinta % 3.6 > 0:
	galoes= int(litros_tinta/3.6)+1
else:
	galoes=litros_tinta/3.6
	#calcular o preço dos galoes quantidade de galões *25
preco=galoes*25
print("Quantidade de galões  ",galoes)
print("preço: ", preco)

