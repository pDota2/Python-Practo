import math

def number_float():
    while True:
        try:
            numS = float(input("Введите число: "))
            return numS
        except ValueError:
            print("Число введено неверно!")

def number_cell():
    while True:
        try:
            numS = int(input("Введите целое положительное число: "))
            if numS < 0:
             raise ValueError
            return numS
        except ValueError:
            print("Число введено неверно!")        

def calculator():
    while True:
        try:
            print("Выберите операцию:")
            print("[1]Сложение")
            print("[2]Вычитание")        
            print("[3]Умножение")
            print("[4]Деление")
            print("[5]Возведение в степень n")
            print("[6]Квадратный корень")
            print("[7]Факториал")
            print("[8]Синус")
            print("[9]Косинус")
            print("[10]Тангенс")
            print("[0]Выход из программы")
        
            command = float(input())
            match command:
                case 1:
                 number1 = number_float()
                 number2 = number_float()
                 print(f"Ответ: {number1 + number2}\n")
                case 2:
                 number1 = number_float()
                 number2 = number_float()
                 print(f"Ответ: {number1 - number2}\n")
                case 3:
                 number1 = number_float()
                 number2 = number_float()
                 print(f"Ответ: {number1 * number2}\n")
                case 4:
                 number1 = number_float()
                 number2 = number_float()
                 if number2 != 0:
                    print(f"Ответ: {number1 / number2}\n")
                 else:
                    print(f"На нуль делить нельзя\n")
                    calculator()
                case 5:
                 number1 = number_float()
                 number2 = number_float()
                 print(f"Ответ: {math.pow(number1, number2)}\n")
                case 6:
                 number1 = number_float()
                 print(f"Ответ: {math.sqrt(number1)}\n")
                case 7:
                 number1 = number_cell()
                 print (f"Ответ: {math.factorial(number1)}\n")
                case 8:
                 number1 = number_float()
                 print(f"Ответ: {math.sin(math.radians(number1))}\n")
                case 9:
                 number1 = number_float()
                 print(f"Ответ: {math.cos(math.radians(number1))}\n")
                case 10:
                 number1 = number_float()
                 print(f"Ответ: {math.tan(math.radians(number1))}\n")
                case 0:
                 exit()
        except ValueError:
            print(f"\nНеизвестная комманда")
calculator()