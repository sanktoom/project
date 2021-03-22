class Bank:

    def __init__(self):
        self.name = input('Введите ваше имя: ')
        self.many = 0
        self.question = {
             '1': "Вы хотите открыть счет '1' - Да/'2' - Нет",
             '2': "Положить деньги на счет-введите     '1' - Положить\n"
                  "Снять деньги со счета-введите       '2' - Снять\n"
                  "Закрыть счет-введите                '3' - Закрыть",
             '3': "Ваш ответ: ",
             '4': "Введите сумму: ",
             '5': "На вашем счету недостаточно средств!"
        }

    def add_many(self, x):
        return self.many + x

    def withdraw_many(self, x):
        return self.many - x

    def show_many(self):
        return "{}, на вашем счету {} грн.".format(self.name, self.many)


try:
    bank = Bank()
    print(bank.question['1'])
    answer = input(bank.question['3'])

    while answer == '1':
        print(bank.show_many())
        print(bank.question['2'])
        _answer = input(bank.question['3'])

        if _answer == '1':
            print(bank.show_many())
            bank.many = bank.add_many(int(input(bank.question['4'])))
        elif _answer == '2':
            print(bank.show_many())
            _many = bank.withdraw_many(int(input(bank.question['4'])))
            if _many >= 0:
                bank.many = _many
            else:
                print(bank.question['5'])
        else:
            break

except ValueError:
    print('Введите число!')