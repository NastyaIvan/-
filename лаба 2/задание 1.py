money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

all_money = money_capital + salary
month = 0
expenses = spend
while all_money >= expenses: 
    #  пока денег хватает на жизнь
    month += 1
    all_money = all_money - expenses + salary
    # вычитаем траты из общего бюджета
    expenses *= 1 + increase
    # увеличение трат каждыйц месяц

print("Количество месяцев, которое можно протянуть без долгов:", month)
