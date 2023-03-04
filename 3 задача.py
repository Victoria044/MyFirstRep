def calculate_salary(years_worked, current_salary):
    if years_worked < 3:
        salary_increase = 0.1
    else:
        salary_increase = 0.2
    
    new_salary = current_salary * (1 + salary_increase)
    
    if new_salary < 4000:
        new_salary += 1000
    else:
        new_salary += 500
    
    return new_salary



def main():
    years_worked = int(input("Введите количество лет работы: "))
    current_salary = int(input("Введите текущую зарплату: "))
    
    new_salary = calculate_salary(years_worked, current_salary)
    
    print("Новая зарплата: ", new_salary)
    
    
if __name__ == '__main__':
    main()