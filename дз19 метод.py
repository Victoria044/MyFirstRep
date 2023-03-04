def divide_by_two_until_less_than_fifty(num):
    count = 0
    
    if num < 50:
        return "Вы ввели слишком маленькое число"
    
    while num >= 50:
        num /= 2
        count += 1
    
    return f"Количество итераций: {count}, число: {num}"

def main():
    num = int(input("Введите число: "))
    result = divide_by_two_until_less_than_fifty(num)
    print(result)

if __name__ == '__main__':
    main()

