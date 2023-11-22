
def profil( nama,alamat,gender,umur,hobi):
    print("nama saya adalah",nama)
    print("alamat saya di",alamat)
    print("gender saya adalah",gender)
    print("umur saya adalah",umur)
    print("Hobi saya", hobi)

profil("Rasyid", "Bogor", "Laki-laki", "18", "bermain bola")


()

print("--- Nomor 2 ---")
def cek_kelulusan(nilai):
    if nilai < 60:
        return "Gagal"
    elif 60 <= nilai <=70:
        return "Baik"
    elif 71 <= nilai <= 80:
        return "Sangat Baik"
    elif 81 <= nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai Tidak Valid" 

# Pemanggilan
print(cek_kelulusan(40))
print("")

()

def ganjil(n):
    for i in range(1, n+1, 2):
        print(i)
#pemanggilan
ganjil(100)