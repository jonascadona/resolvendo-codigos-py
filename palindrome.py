palavra = input("Digite a palavra para verificar se é um palíndromo: ").strip().lower()
palavra_invertida = palavra[::-1]
print(f"A palavra invertida é: {palavra_invertida}")
if palavra == palavra_invertida:
    print("A palava verificada é um palíndromo.")
else:
    print("A palavra verificada não é um palíndromo.")