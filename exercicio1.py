# Escreva um programa que escreva o nome e o ano que o usuário nasceu.
# Depois retorne o nome e sua idade;

def main():

    nome = input("Digite seu nome:")
    print(nome)
    idade = int(input("Digite o ano em que nasceu:"))

    idade = 2023 - idade

    print(idade)

if __name__ == "__main__":
    main()
