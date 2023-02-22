try:
    nama = str(input('Masukkan Nama Lengkap Anda : '))
    prodi = str(input('Masukkan Prodi Anda : '))
    nilai = str(input('Masukkan Nilai(Dalam Huruf) yang Anda Dapat : '))
except ValueError :
    print('Inputan nilai yang anda masukkan tidak valid')

else :
    if nilai == 'E':
        print('Nilai Anda Adalah 0, Kamu niat kuliah engga sih')
    elif nilai == 'D':
        print('Nilai Anda Adalah 1, apakah sudah ada pikiran untuk pindah jurusan?')
    elif nilai == 'C':
        print('Nilai Anda Adalah 2,')
    elif nilai == 'C+':
        print('Nilai Anda Adalah 2.25,')
    elif nilai == 'B':
        print('Nilai Anda Adalah 3.0,')
    elif nilai == "B-":
        print('Nilai Anda Andalah 2.75, kurang belajar nihh')
    elif nilai == 'A':
        print('Nilai Anda Adalah 4.0, tbl tbl serem bgt lohh')
    elif nilai == 'A-':
        print('Nilai Anda Adalah 3.75, kamu keren')

    