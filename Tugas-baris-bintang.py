jumlah_baris = int(input("Masukkan jumlah baris: "))

for baris in range(1, jumlah_baris + 1):
  for kolom in range(baris):
    print("*", end="")
  print()
