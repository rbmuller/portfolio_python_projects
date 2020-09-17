import math

def eval_loop():
    while True:
        x = input("Digite algo e eu irei calcular:")
        if x == 'ultimo':
            print(y, 'Foi o ultimo valor calculado')
        elif x == 'exit':
            break
        else:    
            y = eval(x)
            print(eval(x))

eval_loop()


