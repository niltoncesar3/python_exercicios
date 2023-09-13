entrada = input('Digite [E] para entrar ou [S] para sair: ')
senha = input('Digite a senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha == senha_permitida:
    print('Entrou')
else:
    print('Saiu')