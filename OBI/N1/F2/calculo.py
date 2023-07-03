def soma_dos_digitos(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

S = int(input())
A = int(input())
B = int(input())

N = 0
for i in range(A, B+1):
    if soma_dos_digitos(i) == S:
        N += 1

print(N)
