print("Qual é o valor inicial da integral? (inteiro)")
a = int(input())

print("Qual é o valor final da integral? (inteiro)")
b = int(input())

print("Qual é o valor de n? (inteiro)")
n = int(input())

def function(x):
	return x*x

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
