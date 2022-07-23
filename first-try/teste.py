def isthing(valor):
    if valor == '+' or valor == '-' or valor == '*' or valor == '/':
        return True
    else:
        return False

def operacao():
    global total, num, sinal
    if sinal == '+':
        total += num
    elif sinal == '-':
        total -= num

total = 0
sinal = '+'

while True:
    num = int(input('valor: '))

    operacao()

    sinal = input('sinal: ')
    if sinal == '=':
        print('total:', total)
        break
