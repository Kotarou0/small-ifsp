def menores_contracoes(contracoes, lista):
    contracoes_possiveis = []
    if e_palindromo(lista):
        return contracoes
    for i in range(0, len(lista) - 1):
        contraida = lista.copy()
        contraida[i] = lista[i] + lista[i+1]
        contraida.remove(lista[i+1])
        contracoes_possiveis.append(menores_contracoes(contracoes+1, contraida))
    contracoes = min(contracoes_possiveis)
    return(contracoes)

def e_palindromo(lista):
    for i in range(0, int(len(lista)/2) + 1):
        if lista[i] != lista[len(lista)-i-1]:
            return False
    return True

lista = []
N = int(input())
lista = input().split(" ")
for i in range(0, len(lista)):
    lista[i] = int(lista[i])
print(menores_contracoes(0, lista))
