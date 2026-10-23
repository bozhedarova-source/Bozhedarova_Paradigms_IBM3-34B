import sys
import math

# Ввод коэффициента A 
if len(sys.argv) > 1:
    try:
        A = float(sys.argv[1])
        if A == 0:
            print("Ошибка: А не может быть равен 0.")
            while True:
                try:
                    A = float(input("Введите число А: "))
                    if A != 0:
                        break
                    print("А не может быть равен 0")
                except ValueError:
                    print("Ошибка! Введите число")
    except ValueError:
        print("Некорректное значение А в командной строке.")
        while True:
            try:
                A = float(input("Введите число А: "))
                if A != 0:
                    break
                print("А не может быть равен 0")
            except ValueError:
                print("Ошибка! Введите число")
else:
    while True:
        try:
            A = float(input("Введите число А: "))
            if A != 0:
                break
            print("А не может быть равен 0")
        except ValueError:
            print("Ошибка! Введите число")

# Ввод коэффициента B 
if len(sys.argv) > 2:
    try:
        B = float(sys.argv[2])
    except ValueError:
        print("Некорректное значение B в командной строке.")
        while True:
            try:
                B = float(input("Введите число B: "))
                break
            except ValueError:
                print("Ошибка! Введите число")
else:
    while True:
        try:
            B = float(input("Введите число B: "))
            break
        except ValueError:
            print("Ошибка! Введите число")

# Ввод коэффициента C
if len(sys.argv) > 3:
    try:
        C = float(sys.argv[3])
    except ValueError:
        print("Некорректное значение C в командной строке.")
        while True:
            try:
                C = float(input("Введите число C: "))
                break
            except ValueError:
                print("Ошибка! Введите число")
else:
    while True:
        try:
            C = float(input("Введите число C: "))
            break
        except ValueError:
            print("Ошибка! Введите число")

# Решение уравнения
print(f"\nРешение уравнения: {A}x^4 + {B}x^2 + {C} = 0")
D = B ** 2 - 4 * A * C
print("Дискриминант =", D)

if D < 0:
    print("Действительных решений нет")
elif D == 0:
    y = -B / (2 * A)
    if y > 0:
        x1 = math.sqrt(y)
        x2 = -x1
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif y == 0:
        print("x = 0")
    else:
        print("Действительных решений нет")
else:
    y1 = (-B + math.sqrt(D)) / (2 * A)
    y2 = (-B - math.sqrt(D)) / (2 * A)
    
    roots = []
    if y1 > 0:
        roots.append(math.sqrt(y1))
        roots.append(-math.sqrt(y1))
    elif y1 == 0:
        roots.append(0)
        
    if y2 > 0:
        roots.append(math.sqrt(y2))
        roots.append(-math.sqrt(y2))
    elif y2 == 0:
        roots.append(0)
        
    if len(roots) == 0:
        print("Действительных решений нет")
    else:
        roots = sorted(list(set(roots)))
        for i, root in enumerate(roots, 1):
            print(f"x{i} = {root:.2f}")