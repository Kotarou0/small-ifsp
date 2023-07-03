pessoa = []
for i in range(0, 4):
    pessoa.append(int(input()))

somas = []
for i in range(1, 4):
    somas.append(abs(2*(pessoa[0] + pessoa[i]) - sum(pessoa)))

print(min(somas))
