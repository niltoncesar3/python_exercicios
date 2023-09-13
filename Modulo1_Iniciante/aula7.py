entrada = input('Digite [E] para entrar ou [S] para sair: ')
senha = input ('Digite a senha: ')

senha_permitida = '123456'

if entrada == 'E' and senha_permitida == '123456':
    print('Entrou')
else :
    print('Sair')