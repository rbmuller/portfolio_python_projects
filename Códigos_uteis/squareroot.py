
a = int(input('Deseja saber a raiz quadrada de qual numero? '))
x = int(input('Palpite para a raiz quadrada? '))

while True:
    print(x)
    y = (x + a / x) / 2
    if x == y:
        break
    x = y

print('A raíz quadrada de',a,'é: ',x)    