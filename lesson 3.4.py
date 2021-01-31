def my_func1(x, y):
    if x<0 or y>0:
        print("Error!")
    else:
        print(x**y)
my_func1(x = float(input("Введите число для возведения в степень: ")), y = int(input("Введите степень числа: ")))


def my_func2(x, y):
    if x<0 or y>0:
        print("Error!")
    else:
        b = 1
        for _ in range(abs(y)):
            b/=x
        print(round(b, 4))

my_func2(x = float(input("Введите число для возведения в степень: ")), y = int(input("Введите степень числа: ")))




