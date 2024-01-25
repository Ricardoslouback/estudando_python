#!/usr/bin/env python3
#calcular quantas latas e quanto custa comprar a tinta 
#descobrir a area a ser pintada 

area=int(input("Qual e a area a ser pintada (m)"))
#calcular quantos litros de tinta o cliente precisa (area/6)
litros=area/6
#quantas latas eu vou precisar para quantidad de litros
#calcular quantas latas (litros/18)
#se deu um numero "quebrado" de latas 
#adicionar 1 lata
# se nao 
#de a quantidade de latas 
latas=litros/18
if int(latas) != latas:
	latas=int(latas)+1
	#calcular o preço das latas (quantidade de latas * €80)
preco=latas * 80
print("Quantidade de latas ",latas)
print("preço: ", preco)
	
