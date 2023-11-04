# Escreva um programa de cadastro de usuário, pedindo nome, endereço, cpf, telefone ....
# depois, retorne todas as informações de maneira organizada.

def main():

    nome = input("Digite seu nome: ")
    endereco = input("Digite a rua onde você mora: ")
    numero_endereco = input("Número casa: ")
    bairro = input("Digite o bairro: " )
    cidade = input("Digite a cidade: " )
    cep = input("Digite o CEP: " )
    telefone = input("Digite seu telefone: ")
    email = input("Digite seu e-mail: " )

    texto = f"\n\tgNome completo: {nome}\nRua: {endereco}, {numero_endereco}, {bairro}\nCidade: {cidade}, CEP: {cep}\n Dados de contato: \n Telefone: {telefone}\n E-mail: {email}"

    print(texto)

if __name__ == "__main__":
    main()
