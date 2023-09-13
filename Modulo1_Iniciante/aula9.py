nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}')
    print(f'Sua idade é {idade}')
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é : {nome[0]}')
    print(f'A última letra do seu nome é {nome[-1]}')
    if ' ' in nome:
        print('Contém espaço no seu nome')
    else:
        print('NÃO contém espaço no seu nome')
else:
    print('Algum campo não foi digitado')

    # Exercício
#  Peça ao usuário para digitar seu nome 
#  Peça ao usuário para digitar sua idade
#  Se nome e idade forem digitados :
#      Exiba:
#     Seu nome é {nome}
#     Seu nome tem {n} letras
#     A primeira letra do seu nome é {letra}
#     A última letra do seu nome é {letra}

# Se nada for digitado em nome ou idade:
#     exiba 'Desculpe, você deixou campos vazios'
