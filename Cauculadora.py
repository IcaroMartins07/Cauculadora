def soma(a, b):
    r=a+b
    return r
def subtração(a, b):
    r=a-b
    return r
def multiplicação(a, b):
    r=a*b
    return r
def divisão(a, b):
    r=a/b
    return r
def menu():
    print('''=-=-=-=-=-=-=-=-Cauculadora-=-=-=-=-=-=-=-=
1. Soma
2. Subtração
3. Multiplicação
4. Divisão
5. Sair
''')
    global p, a, b
    print("=-"*30)
    p=int(input('Escolha de 1-5: '))

while True:
    menu()
    if p==5:
        print('Cauculadora Finalizada.')
        break
    print("=-"*30)

    a=int(input('Digite o primeiro valor: '))
    b=int(input('Digite o segundo valor: '))
    print("=-"*30)
    if p==1:
        print(f'o resultado é {soma(a,b)}')
    elif p==2:
        print(f'o resultado é {subtração(a,b)}')
    elif p==3:
        print(f'o resultado é {multiplicação(a,b)}')
    elif p==4:
        print(f'o resultado é {divisão(a,b)}')
    else:
        print('Erro, tente novamente')