n = int(input("Введите натуральное число: "))
result = 0
for i in range(1, n+1):
    if i%2 ==1:
        result+=i
    else:
        result-=i
print(result)