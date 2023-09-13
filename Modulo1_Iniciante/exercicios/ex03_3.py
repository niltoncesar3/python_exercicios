nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome >= 2 and tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 7:
        print('Seu nome é normal')
    else:
        print('Seu nome é grande')
else:
    print('Digite um nome maior que 1 letra')
