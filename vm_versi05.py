# daftar_barang (arr) adalah lit daftar barang yang dijual
# harga_barang (arr) adalah list harga setiap daftar barang
# stok (arr) adalah list ketersediaan stok barang
# nutrisi (arr) adalah list informasi nutrisi barang
# menudipilih (int) adalah inputan pengguna untuk pilihan menu
# sibarang (int) adalah kode barang yang dipilih pengguna
# idbarangdipilih (int) adalah kode inputan pengguna untuk barang yang mau dibeli
# id_barang (int) adalah kode inputan pengguna untuk info nutrisi yang ingin dilihat
# jumlah_pembelian (int) adalah jumlah barang yang ingin dibeli pengguna
# transaksi (int) adalah jumlah transaksi yang harus dibayar pengguna
# nilai_uang (arr) adalah list nominal uang yang dapat digunakan pengguna untuk bertransaksi
# sisa_bayar (arr) adalah jumlah sisa transaksi yang harus dibayar pengguna jika memiliki kembalian
# x_masuk (int) adalah nominal uang yang dimasukkan pengguna
# borong_ngga (int) adalah kode pilihan pengguna untuk memborong atau tidak memborong barang

import colorama
from colorama import Fore, Style
from datetime import datetime

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
print("PILIHAN MENU\n(khusus pilihan 3 hanya bisa dilakukan jika anda Admin): ")
print("\t-------------------------------------------------------------------------------------------------------")
print("\t          1. Membeli        |       2. Info Nutrisi       |    3. Manajemen Data   |     4. Keluar")
print("\t-------------------------------------------------------------------------------------------------------")
print("\n                                         Ketikkan no pilihan menu: ",end="")

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
            #sebelumnya yang dicetak malah stock barang, harusnya jumlah pembelian
            print("   Nilai Transaksi Anda : ( %d x %d ) = %d"%(jumlah_pembelian , harga_barang[idbarangdipilih-1],transaksi))
            print("   -------------------------------------------------------------------------------------------------------")
            print("   Silahkan lakukan pembayaran!")
            sisa_bayar = transaksi

            # PENGGUNAAN ARRAY UNTUK MENDAFTARKAN NILAI MATA UANG YANG DAPAT DIGUNAKAN
            nilai_uang = [500,1000,2000,5000,10000,20000]

            # LOOPING PENGGUNA MEMASUKKAN UANG PEMBAYARAN 
            while sisa_bayar > 0:
                print("   Nilai uang yang Anda Masukan (1. 500 | 2. seribu | 3. 2ribu | 4. 5ribu | 5. 10ribu | 6.20 ribu ): ",end="")
                x_masuk = int(input())
                if x_masuk<=0 or x_masuk > len(nilai_uang):
                    print("   Nilai uang yang anda masukkan tidak valid")
                    continue
                print("   Anda memasukan uang sebesar",nilai_uang[x_masuk-1])
                sisa_bayar = sisa_bayar - nilai_uang[x_masuk-1]
                if sisa_bayar>0:
                    print("   Sudah membayar: %d dan sisa pembayaran: %d, silahkan masukkan kembali uang pembayaran"%(transaksi-sisa_bayar,sisa_bayar))
                elif sisa_bayar==0:
                    print("   Sudah membayar: %d dan Lunas"%(transaksi-sisa_bayar))
                else:
                    print("   Sudah membayar: %d, Lunas dan nilai kembalian: %d, Pembayaran selesai"%(transaksi-sisa_bayar,(-1)*sisa_bayar))
            
            print("   -------------------------------------------------------------------------------------------------------")
            #BAGIAN KEMBALIAN, MENERAPKAN TEKNIK GREEDY AGAR JUMLAH UANG YANG DIKELUARKAN SEDIKIT
            if sisa_bayar<0:
                kembalian =  sisa_bayar*(-1)
                jmlh_lembar_peruang = [0]* len(nilai_uang) #mencatat berapa lembar untuk setiap jenis uang, sebagai kembalian
                i1 = len(nilai_uang)-1 #coba dari nilai uang terbesar
                while kembalian > 0:
                    if kembalian >= nilai_uang[i1]:
                        banyaklembar = kembalian//nilai_uang[i1] 
                        kembalian = kembalian - nilai_uang[i1] * banyaklembar
                        jmlh_lembar_peruang[i1] = banyaklembar
                    i1 = i1 - 1
                
                print("    Kembalian yang dikeluarkan mesin: ",end="")
                for i_jl in range(len(jmlh_lembar_peruang)):
                    if jmlh_lembar_peruang[i_jl] != 0:
                        print("(",jmlh_lembar_peruang[i_jl],"pecahan",nilai_uang[i_jl],")",end=" ")
                print()

            #menyiapkan info untuk update stock
            stok[idbarangdipilih-1]= stok[idbarangdipilih-1]-jumlah_pembelian #stok diupdate
            if stok[idbarangdipilih-1] == 0: 
                print("    Stok barang terupdate, telah habis terjual")
            else:
                print("    Stok barang terupdate, telah terjual:",jumlah_pembelian)
            
            print("    Mesin mengeluarkan %d buah barang %s sesuai transaksi"%(jumlah_pembelian,sibarang))
            print("   -------------------------------------------------------------------------------------------------------")

            #MENULIS KE FILE DATA TRANSAKSI
            f = open("data_transaksi.txt", "a")
            waktu = str(datetime.now())
            f.write(waktu +","+ sibarang+","+str(jumlah_pembelian)+","+str(transaksi)+"\n")
            f.close()

    #kondisi ketika barang kosong        
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

#KONDISI KETIKA MEMILIH MENU 3 (Fungsi Sekunder) 
elif menudipilih==3:
    print(">> Transaksi Manajemen Data")
    print("   Untuk melanjutkan silahkan masukkan username dan password (un pswd): ",end="")
    un,pswd = input().split(" ")
    #print(un,pswd)
    if un=="admin" and pswd=="123":
        print("   Login berhasil\n")
        print("   PILIHAN MENU ADMIN: ")
        print("\t-------------------------------------------------------------------------------------------------------")
        print("\t   1. data transaksi   |     2. add     |     3. edit      |     4. delete     |     5. Keluar")
        print("\t-------------------------------------------------------------------------------------------------------")
        print("\n                                         Ketikkan no pilihan menu admin: ",end="")
        #Input pilihan menu
        menuadminterpilih = int(input())
        
        while menuadminterpilih != 5:
            if menuadminterpilih == 1:
                print("   >>> Melihat data transaksi")
                f = open("data_transaksi.txt", "r")
                nmr = 1
                totTRX = 0
                for baris in f:
                    dataTRX = baris.split(",")
                    print("   %2d. %s    %-15s  %3s  %10s"%(nmr,dataTRX[0],dataTRX[1],dataTRX[2],dataTRX[3]),end="")
                    totTRX = totTRX + int(dataTRX[3])
                    nmr = nmr+1 
                f.close()
                print("    + Total nilai transaksi: ",totTRX)
            elif menuadminterpilih == 2:
                print("   >>> Add data barang baru")
                nm_brng  = input("   Masukkaan data nama barang: ")
                hrg_brng = int(input("   Masukkaan data harga: "))
                stok_brng = int(input("   Masukkaan data stok: "))
                nutri  = input("   Masukkaan data nutrisi barang: ")
                #masukkan ke array
                daftar_barang.append(nm_brng)
                harga_barang.append(hrg_brng)
                stok.append(stok_brng)
                nutrisi.append(nutri)
                print("   Data",nm_brng,"telah tersimpan")
                print("   --------------------------------------------")
                print("    NO.  %15s\t%7s\t%5s"%("  NAMA BARANG  "," HARGA "," STOK "))
                print("   --------------------------------------------")
                for i in range(len(daftar_barang)):
                    print("    %2d.  %-15s\t%7d\t%5d"%(i+1,daftar_barang[i],harga_barang[i],stok[i]))
                print("   --------------------------------------------")

                
            elif menuadminterpilih == 3:
                print("   >>> Edit data barang")
                print("   --------------------------------------------")
                print("    NO.  %15s\t%7s\t%5s"%("  NAMA BARANG  "," HARGA "," STOK "))
                print("   --------------------------------------------")
                for i in range(len(daftar_barang)):
                    print("    %2d.  %-15s\t%7d\t%5d"%(i+1,daftar_barang[i],harga_barang[i],stok[i]))
                print("   --------------------------------------------")
                idtarget = int(input("   Masukkaan nomor barang yang ingin diedit: "))
                print("   Data %s akan diedit."%(daftar_barang[idtarget-1]))
                daftar_barang[idtarget-1]  = input("   Masukkaan data baru nama barang: ")
                harga_barang[idtarget-1] = int(input("   Masukkaan data baru harga: "))
                stok[idtarget-1]  = int(input("   Masukkaan data baru stok: "))
                print("   Proses edit data selesai")

            elif menuadminterpilih == 4:
                print("   >>> Delete data barang")
                print("   --------------------------------------------")
                print("    NO.  %15s\t%7s\t%5s"%("  NAMA BARANG  "," HARGA "," STOK "))
                print("   --------------------------------------------")
                for i in range(len(daftar_barang)):
                    print("    %2d.  %-15s\t%7d\t%5d"%(i+1,daftar_barang[i],harga_barang[i],stok[i]))
                print("   --------------------------------------------")
                idtarget = int(input("   Masukkaan nomor barang yang ingin didelete: "))
                print("   Anda yakin data %s akan didelete ? (y/n): "%(daftar_barang[idtarget-1]),end="")
                keputusan = input()
                if keputusan=='y' or keputusan=='Y':
                    barangyangdidelete = daftar_barang[idtarget-1]
                    daftar_barang.pop(idtarget-1)
                    harga_barang.pop(idtarget-1)
                    stok.pop(idtarget-1)
                    nutrisi.pop(idtarget-1)
                    print("   Data %s telah didelete"%(barangyangdidelete))
                else:
                    print("   Proses delete data %s dibatalkan"%(daftar_barang[idtarget-1]))

            else :
                print("   Pilihan data menu tidak valid. Silahkan masukan kembali")
            print("\n                                         Ketikkan no pilihan menu admin: ",end="")
            #Input lagi pilihan menu
            #----------------------------------------
            f = open("data_aplikasi.csv", "w")
            f.write("")
            f.close()

            #baru append
            f = open("data_aplikasi.csv", "a")
            for i in range(len(daftar_barang)):
                f.write(daftar_barang[i]+", "+str(harga_barang[i])+", "+str(stok[i])+", "+ nutrisi[i].strip()+"\n")
            f.close()
            #---------------------------------------
            menuadminterpilih = int(input())

    else:
        print("   Login gagal, keluar aplikasi")

#KONDISI KETIKA MEMILIH MENU 4 (Fungsi Keluar) 
elif menudipilih == 4:
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
    f.write(daftar_barang[i]+", "+str(harga_barang[i])+", "+str(stok[i])+", "+ nutrisi[i].strip()+"\n")
f.close()
 
