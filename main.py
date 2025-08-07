import json

def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def eh_quadrada(matriz):
    return all(len(linha) == len(matriz) for linha in matriz)

def multiplicar_matrizes(m1, m2):
    n = len(m1)
    resultado = []

    for i in range(n):
        linha = []
        for j in range(n):
            linha.append(0)
        resultado.append(linha)

    print("Multiplicação passo a passo:")
    for i in range(n):
        for j in range(n):
            soma = 0
            for k in range(n):
                mult = multiplicar(m1[i][k], m2[k][j])
                print(f"Multiplicando m1[{i}][{k}]={m1[i][k]} * m2[{k}][{j}]={m2[k][j]} = {mult}")
                soma = somar(soma, mult)
            resultado[i][j] = soma
            print(f"Resultado[{i}][{j}] = {soma}")
    return resultado

def imprimir_matriz(matriz):
    for linha in matriz:
        print(" ".join(str(x) for x in linha))

# Leitura do arquivo
def carregar_matrizes(caminho):
    with open(caminho, "r") as f:
        data = json.load(f)
    return data["matriz1"], data["matriz2"]

if __name__ == "__main__":
    caminho_arquivo = "matrizes.txt"
    matriz1, matriz2 = carregar_matrizes(caminho_arquivo)

    print("Matriz 1:")
    imprimir_matriz(matriz1)

    print("\nMatriz 2:")
    imprimir_matriz(matriz2)

    if not (eh_quadrada(matriz1) and eh_quadrada(matriz2)):
        print("Erro: As matrizes devem ser quadradas.")
    elif len(matriz1) != len(matriz2):
        print("Erro: As matrizes devem ter o mesmo tamanho.")
    else:
        resultado = multiplicar_matrizes(matriz1, matriz2)
        print("\nResultado final:")
        imprimir_matriz(resultado)
