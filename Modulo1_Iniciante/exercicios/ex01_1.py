hora = input('Digite uma hora entre 0h e 23h: ')

try:
    horario = int(hora)
    if horario >= 0 and horario <= 11:
        print('Bom dia')
    elif horario >= 12 and horario <= 17:
        print('Boa tarde')
    elif horario >= 18 and horario <= 23:
        print ('Boa noite')
    else:
        print('Hora inválida')
except:
    print('Digite um número para validar o horário')