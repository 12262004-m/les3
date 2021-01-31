def my_func(a, b, c, max1):
    max1 = max(a, b, c)
    if max1 == a:
        print(max1+max(b, c))
    if max1 == b:
        print(max1+max(a, c))
    if max1 == c:
        print(max1+max(b, a))

my_func(float(input("Введите первое число: ")), float(input("Введите второе число: ")), float(input("Введите третье число: ")), " ")