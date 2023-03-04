age = int(input("Введите возраст: "))

if age < 0:
    print("Неверный возраст")
elif age < 18:
    print("Вы еще не совершеннолетний")
else:
    print("Вы стали взрослым")

