
plat_nomor = str(input('Masukkan Plat Nomor : ')).split
    
try:
    nomor = (plat_nomor)
    if nomor > 0 and nomor < 3000:
        print('Plat nomor tersebut diperuntukan untuk mobil')
    elif plat_nomor >= 3001 and plat_nomor <= 4000:
        print('Plat nomor tersebut diperuntukan untuk motor')
    elif plat_nomor >= 4001 and plat_nomor <= 5000:
        print('Plat nomor tersebut diperuntukan untuk angkatan umum')
    else:
        print('Plat nomor tidak terindifikasi ketiga angkutan tersebut')
except ValueError:
    print('Plat nomor tidak terinditifikasi, setelah kode daerah harus berupa nomor kendaran')
        

