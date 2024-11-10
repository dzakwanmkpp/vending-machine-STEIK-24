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
    harga_barang.append(data[1])
    stok.append(data[2])
    nutrisi.append(data[3])

print(nutrisi)
print(nutrisi[0])