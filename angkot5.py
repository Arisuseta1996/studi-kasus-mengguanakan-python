#  i 1-6 beroperasi
# i 4 dan 10 lembur
#  lainya rusak
# menggunakan if else
# menambahkan 3 lagi rusak

jmlAngkot = 10;
angBeroperasi = 6;

for noAngkot in range(jmlAngkot):
    noAngkot += 1
    if (noAngkot <= angBeroperasi)&(noAngkot != 4)&(noAngkot!=3):
        print(f'Angkot No. {noAngkot} beroperasi dengan baik')
    elif (noAngkot == 10)|(noAngkot == 4):
        print(f'Angkot No. {noAngkot} Lembur')
    else :
        print(f'Angkot No. {noAngkot} tidak beroperasi')
        
    
