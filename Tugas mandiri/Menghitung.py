inputan = input("Inputan: ")

jumlah_angka = 0
jumlah_huruf = 0

for x in inputan:
    if x.isdigit():
        jumlah_angka += 1
    elif x.isalpha():
        jumlah_huruf += 1

print("Jumlah Angka :", jumlah_angka)
print("Jumlah Huruf :", jumlah_huruf)
