import random
import time

def bet(b,g):
    print('Пожалуйста подождите...')
    time.sleep(3)
    choice = random.randint(1, 31)
    if choice == b:
        print('Поздравляю вы выиграли')
        return g * 2
    else:
        print(choice)
        print(f'-{g}$')
        print('Не расстраивайтесь, повезет в другой раз!')

        return 0