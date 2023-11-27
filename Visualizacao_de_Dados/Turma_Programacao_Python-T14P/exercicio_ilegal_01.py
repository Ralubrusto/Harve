# Vamos construir um aplicativo simplificado que executará na linha de comando
# Primeiro escolha um tema! Pode ser um catálogo de filmes, uma loja de ferramentas, um cadastro de clientes...
# O tema é livre, mas aqui está o que precisamos construir:

# Seu código deve gerenciar um conjunto de dados (pessoas, filmes, ferramentas, etc.)
# Cada um desses itens deve ter pelo menos 3 propriedades. Por ex:
#     - Se forem pessoas, cada pessoa pode ter "nome", "idade" e "altura"
#     - Se forem filmes, cada um pode ter "nome", "estilo" e "nota"

# O usuário deve poder realizar as seguintes ações:
# - Listar todos os itens já cadastrados e suas propriedades
# - Inserir um item novo e suas propriedades
# - Deletar um item escolhido pelo usuário



# Para isso seguem algumas dicas

# 01 - O menu deve ser executado com um while. Escolha um caracter para ser a opção de saída ( normalmente usamos "q")
#   Enquanto o usuário não digitar "q", apresente novamente as opções e aguarde pelo input do usuário
# 02 - Separe cada funcionalidade em uma função, e organize a lógica do seu menu chamando essas funções. Fica bem mais organizado
# 03 - Escolha a forma como você irá armazenar os dados de cada item. Pode ser uma lista, um dicionário... basta escolher e estruturar a sua lógica em cima disso


import os

print("Olá, seja bem vindo!")

nome = input("Digite seu nome: ")

os.system("cls")
print(f"Olá {nome.title()}, muito prazer!")
