# Посчитайте манулов от 1 до 100
# 1 2 3 4 5 ...
for i in range(1, 101):
    if i == 1: # если i равно 1?
        print(i, "манул")
    elif i == 2 or i == 3 or i == 4: # иначе если i равно 2, 3 или 4?
        print(i, "манула")
    else:
        print(i, "манулов")
