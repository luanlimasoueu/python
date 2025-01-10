import random

def guessing_game():
    num_aleatorio = random.randint(0, 100)

    num_digitado = int(input(' Qual o número aleatório : '))

    if num_aleatorio > num_digitado:
        print( 'Too high')
    else:
        if num_aleatorio < num_digitado:
            print( 'Too low')
        else:
            if num_aleatorio == num_digitado:
                print( 'Igual')
                guessing_game()

if __name__ == '__main__':
    guessing_game()