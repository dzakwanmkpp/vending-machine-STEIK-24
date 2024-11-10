import colorama
from colorama import Fore, Style
print(Fore.YELLOW,"\n-----------------------------------------------------------------------------------------------------------------------------")
print("                                                 STEI-K 2024 VENDING MACHINE")
print("-----------------------------------------------------------------------------------------------------------------------------")
print(Fore.WHITE)

'''
daftar_barang =["Le Minerale", "Nipis Madu","Pocari Sweat","Teh Botol Sosro", "You C-1000"]
harga_barang =[3600, 2900, 8000, 5000, 6500]
stok =[12, 23, 10, 25, 0]
'''
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


print("DAFTAR BARANG:")
N = len(daftar_barang)
print("----------------------------------------")
print(" NO.  %15s\t%7s\t%5s"%("  NAMA BARANG  "," HARGA "," STOK "))
print("----------------------------------------")
for i in range(N):
    print(" %2d.  %-15s\t%7d\t%5d"%(i+1,daftar_barang[i],harga_barang[i],stok[i]))
print("----------------------------------------")

print()
print("PILIHAN MENU (khusus pilihan 3 sd 6, hanya bisa dilakukan jika anda Admin): ")
print("1. Membeli | 2. Info Nurtisi  \n3. Melihat transaksi yang telah terjadi | 4. Menambah data barang baru | 5. Mengedit data barang | 6. Menghapus data barang ")
print("\nKetikkan no pilihan menu yang ingin anda lakukan: ",end="")
menudipilih = int(input())

if menudipilih == 1:
    print(">> Transaksi pembelian")
    print("   Silahkan masukan no barang yang ingin anda beli: ",end="")
    idbarangdipilih = int(input())
    sibarang = daftar_barang[idbarangdipilih-1]
    if stok[idbarangdipilih-1] > 0:
        print("   Masukkan jumlah kuantitas pembelian (maksimal: %d): "%(stok[idbarangdipilih-1]),end="")
        jumlah_pembelian = int(input())
        if(stok[idbarangdipilih-1] < jumlah_pembelian):
            print("%s hanya tersedia %d buah, Apakah Anda ingin memborong semuanya (1:iya atau 0:tidak)? "%(sibarang,stok[idbarangdipilih-1]),end="")
            borong_ngga = int(input())
            if borong_ngga == 1:
                transaksi = stok[idbarangdipilih-1] * harga_barang[idbarangdipilih-1]
                print("   Nilai Transaksi Anda : ( %d x %d ) = %d"%(stok[idbarangdipilih-1] , harga_barang[idbarangdipilih-1],transaksi))
                print("\n   Silahkan lakukan pembayaran!")
                print("   INGAT! Vending Machine tidak mengeluarkan kembalian, uang kelebihan akan diinfakkan ehehe.")
                sisa_bayar = transaksi
                nilai_uang = [20000,10000,5000,2000,1000,500]
                while sisa_bayar > 0:

                    print("   Nilai uang yang Anda Masukan (1. 20 ribu | 2. 10 ribu | 3. 5 ribu | 4. 2 ribu | 5. seribu | 6. 500 ): ",end="")
                    x_masuk = int(input())
                    print("   Anda memasukan uang sebesar",nilai_uang[x_masuk-1])
                    sisa_bayar = sisa_bayar - nilai_uang[x_masuk-1]
                    if sisa_bayar>0:
                        print("   Sudah membayar: %d dan sisa pembayaran: %d, silahkan masukkan kembali uang pembayaran"%(transaksi-sisa_bayar,sisa_bayar))
                    elif sisa_bayar==0:
                        print("   Sudah membayar: %d dan Lunas"%(transaksi-sisa_bayar))
                    else:
                        print("   Sudah membayar: %d, Lunas dan diinfakkan: %d, silahkan masukkan kembali uang pembayaran"%(transaksi-sisa_bayar,sisa_bayar))
                stok[idbarangdipilih-1] = 0 #stok habis diborong :)
                print("   Stok barang terupdate, telah habis terjual")
            else:
                print("   Transaksi Anda dibatalkan")
        else:
            transaksi = jumlah_pembelian * harga_barang[idbarangdipilih-1]
            print("   Nilai Transaksi Anda : ( %d x %d ) = %d"%(jumlah_pembelian , harga_barang[idbarangdipilih-1],transaksi))
            print("\n   Silahkan lakukan pembayaran!")
            print("   INGAT! Vending Machine tidak mengeluarkan kembalian, uang kelebihan akan diinfakkan ehehe.")
            sisa_bayar = transaksi
            nilai_uang = [20000,10000,5000,2000,1000,500]
            while sisa_bayar > 0:

                print("   Nilai uang yang Anda Masukan (1. 20 ribu | 2. 10 ribu | 3. 5 ribu | 4. 2 ribu | 5. seribu | 6. 500 ): ",end="")
                x_masuk = int(input())
                if x_masuk > len(nilai_uang) or  x_masuk<0:
                    print("   Anda memasukan input yang tidak sesuai (analogi uang tidak terbaca)")
                    continue
                print("   Anda memasukan uang sebesar",nilai_uang[x_masuk-1])
                sisa_bayar = sisa_bayar - nilai_uang[x_masuk-1]
                if sisa_bayar>0:
                    print("   Sudah membayar: %d dan sisa pembayaran: %d, silahkan masukkan kembali uang pembayaran"%(transaksi-sisa_bayar,sisa_bayar))
                elif sisa_bayar==0:
                    print("   Sudah membayar: %d dan Lunas"%(transaksi-sisa_bayar))
                else:
                    print("   Sudah membayar: %d, Lunas dan diinfakkan: %d (Terima kasih sudah berinfaq)."%(transaksi-sisa_bayar,-1*sisa_bayar))
            stok[idbarangdipilih-1]= stok[idbarangdipilih-1]-jumlah_pembelian #stok diupdate
            print("   Stok barang terupdate, telah terjual:",jumlah_pembelian)
            print("   *** Mesin mengeluarkan barang sesuai transaksi ***")
    else:
        print("   Maaf, saat ini %s tidak tersedia."%(sibarang))
    print("")
    
elif menudipilih == 2:
    print(">> Transaksi Mengecek Informasi Nutrisi")
    print("   Silahkan masukan no barang yang ingin anda lihat info nutrisinya: ",end="")
    id_barang = int(input())
    if id_barang >=1 and id_barang <= len(daftar_barang):
        print("   %s, harga : %d, dengan ketersediaan stok: %d"%(daftar_barang[id_barang-1],harga_barang[id_barang-1],stok[id_barang-1]))
        print("   Nutrisi: ",nutrisi[id_barang-1])
elif menudipilih>2 and menudipilih<=6:
    print("Menu pilihan untuk admin under construction :)")
else:
    print("Masukkan anda untuk pilihan menu tidak sesuai")

print("Transaksi Selesai!, silahkan run kembali aplikasi ini untuk transaksi selanjutnya :)\n")

#menulis ke file dengan nilai data barang yang terakhir
#apus dulu
f = open("data_aplikasi.csv", "w")
f.write("")
f.close()

#baru append
f = open("data_aplikasi.csv", "a")
for i in range(len(daftar_barang)):
    #Le Minerale, 3600, 12, tanpa gula + 0 g vit C + kaya mineral alami seperti Ca dan Mg. 
    f.write(daftar_barang[i]+", "+str(harga_barang[i])+", "+str(stok[i])+", "+nutrisi[i])
f.close()
 