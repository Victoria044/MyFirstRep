a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))

if a % b == 0:
    print("Делится, результат:", a // b)
else:
    print("Делится с остатком, остаток:", a % b)
