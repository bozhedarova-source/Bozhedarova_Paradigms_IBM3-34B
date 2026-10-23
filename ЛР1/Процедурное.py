import sys
import math

def get_coefficient(name, index, is_zero_forbidden=False):
    if len(sys.argv) > index:
        try:
            val = float(sys.argv[index])
            if is_zero_forbidden and val == 0:
                print(f"Ошибка: {name} не может быть равен 0.")
            else:
                return val
        except ValueError:
            print(f"Некорректное значение {name} в командной строке.")
    
    while True:
        try:
            val = float(input(f"Введите число {name}: "))
            if is_zero_forbidden and val == 0:
                print(f"{name} не может быть равен 0")
                continue
            return val
        except ValueError:
            print("Ошибка! Введите число")

def solve_biquadratic(a, b, c):
    print(f"\nРешение уравнения: {a}x^4 + {b}x^2 + {c} = 0")
    d = b ** 2 - 4 * a * c
    print("Дискриминант =", d)

    if d < 0:
        print("Действительных решений нет")
        return

    if d == 0:
        y = -b / (2 * a)
        if y > 0:
            x = math.sqrt(y)
            print(f"x1 = {x}")
            print(f"x2 = {-x}")
        elif y == 0:
            print("x = 0")
        else:
            print("Действительных решений нет")
    else:
        y1 = (-b + math.sqrt(d)) / (2 * a)
        y2 = (-b - math.sqrt(d)) / (2 * a)
        
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
            
        if not roots:
            print("Действительных решений нет")
        else:
            roots = sorted(list(set(roots)))
            for i, root in enumerate(roots, 1):
                print(f"x{i} = {root}")

A = get_coefficient("A", 1, is_zero_forbidden=True)
B = get_coefficient("B", 2)
C = get_coefficient("C", 3)
    
solve_biquadratic(A, B, C)