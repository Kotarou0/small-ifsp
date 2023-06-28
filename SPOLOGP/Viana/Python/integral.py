import math
import os

os.system('clear')

#print("Qual é a função que você quer integrar? (em termos de x)")
#expression = input()
expression = "(math.e)**(-(x**2))"

a = ""
while type(a) != float:
	print("Qual é o valor inicial da integral?")
	try:
		a = float(input())
	except:
		print("Por favor, digite um número. Tente novamente.\n")

b = ""
while type(b) != float:
	print("Qual é o valor final da integral?")
	try:
		b = float(input())
	except:
		print("Por favor, digite um número. Tente novamente.\n")

n = ""
while type(n) != float:
	print("Em quantos retângulos você quer dividir a função? (número positivo)")
	try:
		n = float(input())
		if n == 0:
			print("Por favor, digite um número positivo. Tente novamente.\n")
			n = ""
	except:
		print("Por favor, digite um número inteiro. Tente novamente.\n")

def function(x):
	try:
		return eval(expression)
	except:
		print("Os valores digitados estão fora do domínio da função ou não estão definidos. Por favor, tente novamente.")
		quit()

points = []
integral = 0

i = 0
dx = (b-a)/n
while i < n:
	x = a + i*dx
	points.append([x, function(x)])
	i += 1

for pair in points:
	integral += pair[1]*dx

print("O valor aproximado da integral é: ", integral)
