# N = int(input())
#
# if N%10 > 5:
#     print("Hello")
# else:
#     print("Мало единиц")

# Посчитайте сумму чисел от 1 до N
# 1 + 2 + 3 + ... + N
N = 10
summ = 0
for i in range(1, N + 1):
    print(i)
    summ += i
print(summ)