import random


def guessing_game(n):

    if n > 0: 
        num_aleatorio = random.randint(0, 100)

        num_digitado = int(input(' Qual o número aleatório : '))

        n = n - 1

        if num_aleatorio > num_digitado:
            print( 'Too loo')
            guessing_game(n)
        else:
            if num_aleatorio < num_digitado:
                print( 'Too hight')
                guessing_game(n)
            else:
                if num_aleatorio == num_digitado:
                    print( 'Igual')
                    
                    

if __name__ == '__main__':
    guessing_game( 3 )