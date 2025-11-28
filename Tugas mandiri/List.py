list1 = [13, 15, 30, 41, 45, 55, 75, 95, 102, 135, 139, 151, 193, 200]

for x in list1:
    if x > 151:
        continue
    if x % 3 == 0:
        print(x)
