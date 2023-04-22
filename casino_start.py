from decouple import config
from casino_logic import bet

MY_MONEY = int(config('MY_MONEY'))
while True:
    print('Ваш баланс равен' + str(MY_MONEY))
    print('Чтобы запустить казино нажмите (да)/Чтобы выйти, тогда (нет)')
    a = input('')
    if a == 'нет':
        print('Вы вышли!\Желаете сыграть?')
        break
    elif a == 'да':
        b = int(input('Загадайте число от 1 до 30: '))
        g = int(input('Какую ставку вы желаете сделать? '))
        MY_MONEY -= g
        MY_MONEY += bet(b,g)
    else:
        print('Проверьте, все ли верно вы написали')

