def soma_dos_digitos(n):
    pass

S = int(input())
A = int(input())
B = int(input())

N = 0
for i in range(A, B+1):
    if soma_dos_digitos(i) == S:
        N += 1

print(N)
