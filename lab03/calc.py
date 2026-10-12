def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b
if __name__ == "__main__":
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    print(f"Результат: {add(num1, num2)}")
    print(f"Вычитание: {sub(num1, num2)}")
    print(f"Умножение: {mul(num1, num2)}")
    print(f"Деление: {div(num1, num2)}")
