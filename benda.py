print("menjelaskan merk baju")
print("berikut adalah penjelasannya")
baju = []

nama_merk = input("masukan nama merk :")
baju.append(nama_merk)

target_pasar = input("siapa target penjualan : ")
baju.append(target_pasar)

warna = input("warna apa saja yang dijual :")
baju.append(warna)

tahun_rilis = int(input("tahun rilis :"))
baju.append(tahun_rilis)

lebar_baju = float(input("lebar baju :"))
baju.append(lebar_baju)

panjang_baju = float(input("panjang baju :"))
baju.append(panjang_baju)

ukuran = input("kategori ukuran :")
baju.append(ukuran) 
print ("erigo adalah merk baju, yang dikhususkan untuk remaja, memiliki warna hitam dan putih, 2011 adalah tahun rilisnya,"eri
 "jika panjangnya 57.5 dan lebar 53.5 itu adalah kategori ukuran L")

print(baju)