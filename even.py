# Вывести все четные числа от 1 до 20
# 1 2 3 4 5
# 1 3 5 7 9 11
for i in range(2, 21):
    if i % 2 == 0:
        print(i)

for i in range(2, 21, 2):
    print(i)