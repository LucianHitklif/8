n = int(input("Введите, сколько натуральных чисел будет: "))
max1 = 0
max2 = 0
for i in range (n):
    number = int(input("Введите сами числа: "))
    if number>max1:
        max2=max1
        max1=number
    elif number>max2:
        max2=number
print(max1)
print(max2)