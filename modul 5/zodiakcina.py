shio = ["Monyet", "Ayam", "Anjing", "Babi", "Tikus", "Kerbau",
        "Macan", "Kelinci", "Naga", "Ular", "Kuda", "Kambing"]

tahun = int(input("Masukkan tahun lahir: "))
print("Shio kamu adalah:", shio[tahun % 12])
