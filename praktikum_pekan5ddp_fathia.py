# TUGAS 1
kendaraan = ['Honda', 'Motor', '200', 'pink', '2']
print(kendaraan)

kendaraan.append('13jt')
kendaraan.append('matic')
print(kendaraan)

kendaraan.insert(2,'Honda')
print(kendaraan)

print(type(kendaraan))
print(type(kendaraan[0]))
print(type(kendaraan[1]))
print(type(kendaraan[2]))
print(type(kendaraan[3]))
print(type(kendaraan[4]))
print(type(kendaraan[5]))
print(type(kendaraan[6]))
print(type(kendaraan[7]))

# TUGAS 2
menghitung_luas = int(input(""""Pilih Salah Satu 
                        1. Hitung Luas Persegi
                        2. Hitung Luas Lingkaran
                        3. Hitung Luas Segitiga
                        """))
print(menghitung_luas)

match menghitung_luas:
    case 1 :
        print('menghitung Luas Persegi')
        sisi = int(input('masukkan nilai sisi:'))
        hitung_luas_persegi = sisi**2
        print(f'jadi luas persegi dengan sisi {sisi} cm adalah {hitung_luas_persegi} cm^2')
    case 2 :
        print('menghitung Luas Lingkaran')
        jari_jari = int(input('masukkan nilai diameter:'))
        pi = 22/7
        hitung_luas_lingkaran = 22/7*jari_jari**2
        print(f'jadi luas lingkaran dengan sisi {jari_jari} cm adalah {hitung_luas_lingkaran} cm^2')
    case 3 :
        print('menghitung Luas Segitiga')
        tinggi = int(input('masukkan nilai tinggi:'))
        alas = int(input('masukkan nilai alas:'))
        hitung_luas_segitiga = alas*tinggi*0.5
        print(f'jadi luas segitiga dengan sisi {alas} cm {tinggi} adalah {hitung_luas_segitiga} cm^2')
    case _:
        print('pilihan tidak valid')