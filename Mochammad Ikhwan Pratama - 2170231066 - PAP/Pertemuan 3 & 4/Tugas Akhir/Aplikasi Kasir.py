print("          Mampir Kuy          ")
print("===============================")

menu = {
    "Fried Chicken":15000,
    "Burger Queen":25000,
    "French Fries":10000,
    "Green Tea Latte":12000,
    "Millshake":15000,
}
print("========= Daftar Menu =========")
for i in menu:
    print("Daftar Menu : ", i, "\t harga : ",menu[i])
print("======================================================")
print("==========Pembelian diatas 100000 diskon 15%==========")
nama = input("Nama Pelanggan :")
alamat = input("Alamat Pelanggaan :")
no_tlp = input("Mo tlp Pelanggan :")
tanggal = input("Tanggal Pembelian :")
beli = input("Pilih Menu :")
jumlah = int(input("Jumlah Pesanan :"))
bayar = jumlah * menu[beli]

if bayar > 100000:
    diskon = bayar*15/100
    total = bayar - diskon
else:
    total = bayar
    
print("========= Detail Pembayaran =========")
print("menu yang di pesan : ",beli)
print("Jumlah yang di pesan : ",jumlah)
print("Total biaya : ",bayar)
print("Total yang harus dibayar : ", total)