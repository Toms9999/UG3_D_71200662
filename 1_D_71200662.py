curah_hujan = float(input('Masukkan nilai curah hujan : '))

if curah_hujan == 0 :
    print('Cuaca terang/berawan')
elif curah_hujan > 0.5 and curah_hujan <= 20:
    print('Curah hujan ringan')
elif curah_hujan > 21 and curah_hujan <= 50:
    print('Curah hujan sedang')
elif curah_hujan > 51 and curah_hujan<= 100:
    print('Curah hujan lebat')
else : 
    curah_hujan > 101
    print('Curah hujan extrime')
