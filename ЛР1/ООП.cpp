#include <iostream>
#include <cmath>
#include <cstdlib>

class BiquadraticEquation {
private:
    double a, b, c;

    double inputCoefficient(char name, int index, bool checkZero, int argc, char* argv[]) {
        double value;

        if (index < argc) {
            value = atof(argv[index]);

            if (value == 0 && argv[index][0] != '0') {
                std::cout << "Некорректное значение " << name << " в командной строке." << std::endl;
            } else {
                if (checkZero && value == 0) {
                    std::cout << name << " не может быть равен 0" << std::endl;
                } else {
                    return value;
                }
            }
        }

        while (true) {
            std::cout << "Введите число " << name << ": ";
            std::cin >> value;

            if (std::cin.fail()) {
                std::cin.clear();
                std::cin.ignore(10000, '\n');
                std::cout << "Ошибка! Введите число" << std::endl;
                continue;
            }

            if (checkZero && value == 0) {
                std::cout << name << " не может быть равен 0" << std::endl;
                continue;
            }

            return value;
        }
    }

public:
    void input(int argc, char* argv[]) {
        a = inputCoefficient('A', 1, true, argc, argv);
        b = inputCoefficient('B', 2, false, argc, argv);
        c = inputCoefficient('C', 3, false, argc, argv);
    }

    void solve() {
        std::cout << "\nРешение уравнения: " << a << "x^4 + " << b << "x^2 + " << c << " = 0" << std::endl;

        double d = b * b - 4 * a * c;
        std::cout << "Дискриминант = " << d << std::endl;

        if (d < 0) {
            std::cout << "Действительных решений нет" << std::endl;
        }
        else if (d == 0) {
            double y = -b / (2 * a);

            if (y > 0) {
                double x = sqrt(y);
                std::cout << "x1 = " << x << std::endl;
                std::cout << "x2 = " << -x << std::endl;
            }
            else if (y == 0) {
                std::cout << "x = 0" << std::endl;
            }
            else {
                std::cout << "Действительных решений нет" << std::endl;
            }
        }
        else {
            double y1 = (-b + sqrt(d)) / (2 * a);
            double y2 = (-b - sqrt(d)) / (2 * a);

            double roots[4];
            int count = 0;

            if (y1 > 0) {
                roots[count] = sqrt(y1);
                count++;
                roots[count] = -sqrt(y1);
                count++;
            }
            else if (y1 == 0) {
                roots[count] = 0;
                count++;
            }

            if (y2 > 0) {
                roots[count] = sqrt(y2);
                count++;
                roots[count] = -sqrt(y2);
                count++;
            }
            else if (y2 == 0) {
                roots[count] = 0;
                count++;
            }

            if (count == 0) {
                std::cout << "Действительных решений нет" << std::endl;
            }
            else {
                for (int i = 0; i < count - 1; i++) {
                    for (int j = 0; j < count - i - 1; j++) {
                        if (roots[j] > roots[j + 1]) {
                            double temp = roots[j];
                            roots[j] = roots[j + 1];
                            roots[j + 1] = temp;
                        }
                    }
                }

                int num = 1;
                std::cout << "x" << num << " = " << roots[0] << std::endl;

                for (int i = 1; i < count; i++) {
                    if (roots[i] != roots[i - 1]) {
                        num++;
                        std::cout << "x" << num << " = " << roots[i] << std::endl;
                    }
                }
            }
        }
    }
};

int main(int argc, char* argv[]) {
    BiquadraticEquation equation;
    equation.input(argc, argv);
    equation.solve();

    return 0;
}
