print("Ведите 10 чисел: ")
result = 'YES'
for i in range(10):
    number = int(input())
    if number%2 !=0:
        result = 'NO'
print(f'Все числа четные? - {result}')