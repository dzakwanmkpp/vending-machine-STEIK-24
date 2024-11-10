import colorama
from colorama import Fore, Style
print(Fore.YELLOW,"\n-----------------------------------------------------------------------------------------------------------------------------")
print("                                                 STEI-K 2024 VENDING MACHINE")
print("-----------------------------------------------------------------------------------------------------------------------------")
print(Fore.WHITE)

#baca data dari file : data_aplikasi.dat
f = open("data_aplikasi.csv", "r")
daftar_barang =[]
harga_barang =[]
stok =[]
nutrisi = []
for baris in f:
    #print(baris)
    data = baris.split(",")
    #print(data)
    daftar_barang.append(data[0])
    harga_barang.append(int(data[1]))
    stok.append(int(data[2]))
    nutrisi.append(data[3])
f.close()

#menampilkan data barang
print("DAFTAR BARANG:")
N = len(daftar_barang)
print("----------------------------------------")
print(" NO.  %15s\t%7s\t%5s"%("  NAMA BARANG  "," HARGA "," STOK "))
print("----------------------------------------")
for i in range(N):
    print(" %2d.  %-15s\t%7d\t%5d"%(i+1,daftar_barang[i],harga_barang[i],stok[i]))
print("----------------------------------------")

#menampilkan menu aplikasi
print()
print("PILIHAN MENU\n(khusus pilihan 3 sd 6, hanya bisa dilakukan jika anda Admin): ")
print("\t1. Membeli        |  3. Data transaksi yang telah terjadi  |  5. Mengedit data barang  |  7. Keluar aplikasi")
print("\t2. Info Nurtisi   |  4. Menambah data barang baru          |  6. Menghapus data barang ")
print("\nKetikkan no pilihan menu yang ingin anda lakukan: ",end="")

#Input pilihan menu
menudipilih = int(input())

#MENENTUKAN AKSI SESUAI KONDISI MENU YANG DIPILIH
#KONDISI KETIKA MEMILIH MENU 1 (MEMBELI)
if menudipilih == 1:
    print(">> Transaksi pembelian")
    print("   Silahkan masukan no barang yang ingin anda beli: ",end="")
    idbarangdipilih = int(input())
    sibarang = daftar_barang[idbarangdipilih-1]
    transaksi = 0
    if stok[idbarangdipilih-1] > 0:
        print("   Masukkan jumlah kuantitas pembelian (maksimal: %d): "%(stok[idbarangdipilih-1]),end="")
        jumlah_pembelian = int(input())
        if(stok[idbarangdipilih-1] < jumlah_pembelian):
            print("   %s hanya tersedia %d buah, Apakah Anda ingin memborong semuanya (1:iya atau 0:tidak)? "%(sibarang,stok[idbarangdipilih-1]),end="")
            borong_ngga = int(input())
            if borong_ngga == 1:
                transaksi = stok[idbarangdipilih-1] * harga_barang[idbarangdipilih-1]
                jumlah_pembelian =  stok[idbarangdipilih-1] #stok habis diborong :)
            else:
                print("   Transaksi Anda dibatalkan")
        else:
            transaksi = jumlah_pembelian * harga_barang[idbarangdipilih-1]
        
        #Proses pembayaran hanya dilakukan jika ada transaksi
        if transaksi != 0:
            print("   Nilai Transaksi Anda : ( %d x %d ) = %d"%(stok[idbarangdipilih-1] , harga_barang[idbarangdipilih-1],transaksi))
            print("\n   Silahkan lakukan pembayaran!")
            print("   INGAT! Vending Machine tidak mengeluarkan kembalian, uang kelebihan akan diinfakkan ehehe.")
            sisa_bayar = transaksi

            # PENGGUNAAN ARRAY UNTUK MENDAFTARKAN NILAI MATA UANG YANG DAPAT DIGUNAKAN
            nilai_uang = [500,1000,2000,5000,10000,20000]

            # LOOPING PENGGUNA MEMASUKKAN UANG PEMBAYARAN 
            while sisa_bayar > 0:
                print("   Nilai uang yang Anda Masukan (1. 500 | 2. seribu | 3. 2ribu | 4. 5ribu | 5. 10ribu | 6.20 ribu ): ",end="")
                x_masuk = int(input())
                if x_masuk<0 or x_masuk >= len(nilai_uang):
                    print("   Nilai uang yang anda masukkan tidak valid")
                    continue
                print("   Anda memasukan uang sebesar",nilai_uang[x_masuk-1])
                sisa_bayar = sisa_bayar - nilai_uang[x_masuk-1]
                if sisa_bayar>0:
                    print("   Sudah membayar: %d dan sisa pembayaran: %d, silahkan masukkan kembali uang pembayaran"%(transaksi-sisa_bayar,sisa_bayar))
                elif sisa_bayar==0:
                    print("   Sudah membayar: %d dan Lunas"%(transaksi-sisa_bayar))
                else:
                    print("   Sudah membayar: %d, Lunas dan diinfakkan: %d, Pembayaran selesai"%(transaksi-sisa_bayar,(-1)*sisa_bayar))
            
            #menyiapkan info untuk update stock
            stok[idbarangdipilih-1]= stok[idbarangdipilih-1]-jumlah_pembelian #stok diupdate
            if stok[idbarangdipilih-1] == 0: 
                print("   Stok barang terupdate, telah habis terjual")
            else:
                print("   Stok barang terupdate, telah terjual:",jumlah_pembelian)
            print("   *** Mesin mengeluarkan barang sesuai transaksi ***")
    else:
        print("   Maaf, saat ini %s tidak tersedia."%(sibarang))
    print("")

#OPSI KETIKA MEMILIH MENU 2 (MENAMPILKAN INFO NUTRISI)    
elif menudipilih == 2:
    print(">> Transaksi Mengecek Informasi Nutrisi")
    print("   Silahkan masukan no barang yang ingin anda lihat info nutrisinya: ",end="")
    id_barang = int(input())
    if id_barang >=1 and id_barang <= len(daftar_barang):
        print("   %s, harga : %d, dengan ketersediaan stok: %d"%(daftar_barang[id_barang-1],harga_barang[id_barang-1],stok[id_barang-1]))
        print("   Nutrisi: ",nutrisi[id_barang-1])
#KONDISI KETIKA MEMILIH MENU 3-6 (Fungsi Sekunder) 
elif menudipilih>2 and menudipilih<=6:
    print("Menu pilihan untuk admin under construction :)")
#KONDISI KETIKA MEMILIH MENU 7 (Fungsi Keluar) 
elif menudipilih == 7:
    print("Anda memilih keluar aplikasi")
#KONDISI KETIKA MEMILIH MENU 7 (Fungsi Keluar) 
else:
    print("Masukkan anda untuk pilihan menu tidak sesuai")

print("Transaksi Selesai! silahkan run kembali aplikasi ini untuk transaksi selanjutnya :)\n")

#OPERASI FILE UNTUK MENDUKUNG UPDATE DATA STOCK
#menulis ke file dengan nilai data barang yang terakhir
#apus dulu
f = open("data_aplikasi.csv", "w")
f.write("")
f.close()

#baru append
f = open("data_aplikasi.csv", "a")
for i in range(len(daftar_barang)):
    # Le Minerale, 3600, 12, tanpa gula + 0 g vit C + kaya mineral alami seperti Ca dan Mg. 
    # print(daftar_barang[i]+", "+str(harga_barang[i])+", "+str(stok[i])+", "+ nutrisi[i].strip())
    f.write(daftar_barang[i]+", "+str(harga_barang[i])+", "+str(stok[i])+", "+ nutrisi[i].strip()+"\n")
f.close()
 