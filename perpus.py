def pustaka():
    print('''
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
─██████████████─██████──██████─██████████████─██████████████─██████████████─██████──████████─██████████████─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░██─██░░░░░░░░░░██─
─██░░██████░░██─██░░██──██░░██─██░░██████████─██████░░██████─██░░██████░░██─██░░██──██░░████─██░░██████░░██─
─██░░██──██░░██─██░░██──██░░██─██░░██─────────────██░░██─────██░░██──██░░██─██░░██──██░░██───██░░██──██░░██─
─██░░██████░░██─██░░██──██░░██─██░░██████████─────██░░██─────██░░██████░░██─██░░██████░░██───██░░██████░░██─
─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░██─────██░░██─────██░░░░░░░░░░██─██░░░░░░░░░░██───██░░░░░░░░░░██─
─██░░██████████─██░░██──██░░██─██████████░░██─────██░░██─────██░░██████░░██─██░░██████░░██───██░░██████░░██─
─██░░██─────────██░░██──██░░██─────────██░░██─────██░░██─────██░░██──██░░██─██░░██──██░░██───██░░██──██░░██─
─██░░██─────────██░░██████░░██─██████████░░██─────██░░██─────██░░██──██░░██─██░░██──██░░████─██░░██──██░░██─
─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██─────██░░██─────██░░██──██░░██─██░░██──██░░░░██─██░░██──██░░██─
─██████─────────██████████████─██████████████─────██████─────██████──██████─██████──████████─██████──██████─
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-
''')

def menu_utama():
    pustaka()
    print(f'''               Selamat Datang di App Admin Pustaka,

                        
                            Menu Utama :
                            1. Daftar Buku Pustaka
                            2. Menambah Buku
                            3. Sunting Daftar Buku
                            4. Menghapus Buku dari Daftar
                            5. Keluar''')

    pilihan = cek_pilihan(5)
    
    if pilihan == '1':
        menu_1(daftar_buku_perpus)
    elif pilihan == '2':
        menu_2(daftar_buku_perpus)
    elif pilihan == '3':
        menu_3(daftar_buku_perpus)
    elif pilihan == '4':    
        menu_4(daftar_buku_perpus)
    elif pilihan == '5':
        yakin = yakinkah()
        if yakin == 'y':
            quit()
        elif yakin =='n':
            print('Pilihan yg anda masukkan salah')
            menu_utama()
            
# Menampilkan Database Perpus dalam Tabel
def buku_perpus(daftar):
    print('''
    Daftar Buku

    | ID | Stok\t| Buku
    ''',end='')

    for n in range(len(daftar['ID'])):
        print(f'''
    | {daftar['ID'][n]}  | {daftar['Stok'][n]}\t| {daftar['Judul'][n]}\t
        \t  {daftar['Pengarang'][n]}, {daftar['Tahun Terbit'][n]}
    ''', end='')

# Mengeluarkan Database untuk 1 index
def cari_1(daftar, input):
    print('''
    Daftar Buku

    | ID | Stok\t| Buku
    ''',end='')
    n = daftar['ID'].index(input)

    print(f'''
    | {daftar['ID'][n]}  | {daftar['Stok'][n]}\t| {daftar['Judul'][n]}\t
        \t  {daftar['Pengarang'][n]}, {daftar['Tahun Terbit'][n]}
    ''', end='')
    return n

# daftar_buku_perpus = {
# 'ID':[],
# 'Stok':[],
# 'Judul':[],
# 'Pengarang':[],
# 'Tahun Terbit':[],
# }

# Database Buku Perpus
daftar_buku_perpus = {
'ID':['1','2','3'],
'Stok':['2','3','4'],
'Judul':['Atomic Habits', 'The Little Book That Still Beats the Market', 'Rage'],
'Pengarang':['James Clear', 'Joel Greenblatt', 'Stephen King'],
'Tahun Terbit':['2018', '2010', '1977']
}

# Helper Function
def yakinkah():
    yakinkah = input('Apakah anda yakin? (Y/N)')
    while (yakinkah != 'y') and (yakinkah != 'n'):
        print('\nMasukan pilihan "Y" atau "N" ')
        yakinkah = (input('Apakah anda yakin ? (Y/N)')).lower()
    return yakinkah

def cek_numeric(pertanyaan_input):
    input_num = input(f'{pertanyaan_input}')
    cek_num = input_num.isnumeric()
    while cek_num == False:
        print('Input harus berupa angka\n') 
        input_num = input(f'{pertanyaan_input}')
        cek_num = input_num.isnumeric()
    return input_num

def cek_pilihan(banyak_pilihan):
    pilihan = input('Masukan nomor pilihan anda : ')
    n_pilihan = []
    for n in range(1,banyak_pilihan+1):
        n_pilihan.append(str(n))
    while pilihan not in n_pilihan:
        print('Masukkan pilihan yang tersedia\n')
        pilihan = (input('Masukan pilihan yang tersedia :'))      
    return pilihan

# Menu 1 : Daftar Buku Pustaka
def menu_1(daftar):
    print(f'''
     -+-+-+-                                            -+-+-+-
    -+-+- App Admin Pustaka : Menu 1 [Daftar Buku Pustaka] -+-+-
     -+-+-+-                                            -+-+-+-

    1. Menampilkan seluruh daftar
    2. Menampilkan daftar spesifik
    3. Keluar ke Halaman Utama
    ''')

    pilihan = cek_pilihan(3)

    if pilihan == '1':
        if len(daftar['ID']) == 0:
            print('Tidak Ada Data')
            menu_1(daftar) 
            
        buku_perpus(daftar_buku_perpus)
        menu_1(daftar)

    elif pilihan == '2':
        if len(daftar['ID']) == 0: 
            print('Tidak Ada Data')
            menu_1(daftar)

        input_id = cek_numeric('Masukan ID buku yang ingin anda lihat: \n')    

        if input_id not in daftar['ID']:
            print('Tidak Ada Data')
            menu_1(daftar)
            
        cari_1(daftar, input_id)
        menu_1(daftar)
        
    else:
        yakin = yakinkah()
        if yakin =='n':
            menu_1(daftar)
        elif yakin =='y':
            menu_utama()

# Menu 2 : Menambah Buku
def menu_2(daftar):
    print(f'''
     -+-+-+-                                      -+-+-+-
    -+-+- App Admin Pustaka : Menu 2 [Menambah Buku] -+-+-
     -+-+-+-                                      -+-+-+-

    1. Menambah Buku
    2. Keluar ke Halaman Utama
    ''')
    
    pilihan = cek_pilihan(2)
    
    if pilihan == '1':        
        input_id = cek_numeric('Masukan ID buku yang ingin ditambahkan : ')        
        if input_id in daftar['ID']:
            print('\nData sudah ada')
            menu_2(daftar)

        else:
            input_stok = cek_numeric('Masukan jumlah buku : ')
            input_judul = input('Masukan judul buku : ')
            input_pengarang = input('Masukan nama pengarang : ')
            input_tahun = cek_numeric('Masukan tahun terbit : ')
            yakin = yakinkah()
            if yakin =='n':
                menu_2(daftar)

            elif yakin =='y':
                daftar['ID'].append(input_id)
                daftar['Stok'].append(input_stok)
                daftar['Judul'].append(input_judul)
                daftar['Pengarang'].append(input_pengarang)
                daftar['Tahun Terbit'].append(input_tahun)
                print('---Data Tersimpan---')
                menu_2(daftar)

    elif pilihan == '2':
        yakin = yakinkah()
        if yakin == 'y':
            menu_utama()
        else:
            menu_2(daftar)

# Menu 3 : Sunting Daftar Buku
def menu_3(daftar):
    print(f'''
     -+-+-+-                                     -+-+-+-
    -+-+- App Admin Pustaka : Menu 3 [Sunting Buku] -+-+-
     -+-+-+-                                     -+-+-+-

    1. Sunting Buku
    2. Keluar ke Halaman Utama
    ''')
    
    pilihan = cek_pilihan(2)

    if pilihan == '1':
        input_id = input('Masukan ID Buku yang ingin di update :')
        if input_id not in daftar['ID']:
            print('\nData yang anda cari tidak ada')
            menu_3(daftar)
        elif input_id in daftar['ID']:
            index_input = cari_1(daftar,input_id)

            yakin = yakinkah()
            if yakin == 'n':
                menu_3(daftar)
            elif yakin =='y':
                print('''Data yang ingin update:
                    1. Stok
                    2. Judul
                    3. Pengarang
                    4. Tahun Terbit''')
                    
                pilihan = cek_pilihan(5)

                pilihan = int(pilihan)
                opsi = ["Stok", "Judul", "Pengarang", "Tahun Terbit"] 
                if pilihan in [1,4,5]:                                      
                    input_baru = cek_numeric(f'Masukan {opsi[pilihan-1]} baru : ')
                else:                 
                    input_baru = input(f'Masukan {opsi[pilihan-1]} baru : ')                        

                yakin = yakinkah()
                    
                if yakin == 'n':
                    menu_3(daftar)
                elif yakin == 'y':

                    daftar[opsi[pilihan-1]][index_input] = input_baru
                    print('---Data telah terupdate---')
                    menu_3(daftar)

    elif pilihan == '2':
        yakin = yakinkah()
        if yakin == 'y':
            menu_utama()
        elif yakin =='n':
            menu_3(daftar)

# Menu 4 : Menghapus Buku dari daftar
def menu_4(daftar):
    print(f'''
     -+-+-+-                                       -+-+-+-
    -+-+- App Admin Pustaka : Menu 4 [Menghapus Data] -+-+-
     -+-+-+-                                       -+-+-+-

    1. Menghapus Daftar Buku
    2. Keluar ke Halaman Utama
    ''')

    pilihan = cek_pilihan(2)
    
    if pilihan == '1':

        input_id = cek_numeric('Masukan ID Buku yang datanya ingin dihapus :')
            
        if input_id not in daftar['ID']:
            print('\nData yang anda cari tidak ada')
            menu_4(daftar)

        elif input_id in daftar['ID']:
            indeks = cari_1(daftar,input_id)

            yakin = yakinkah()

            if yakin == 'n':
                menu_4(daftar)
            elif yakin =='y':
                daftar['ID'].pop(indeks)
                daftar['Stok'].pop(indeks)
                daftar['Judul'].pop(indeks)
                daftar['Pengarang'].pop(indeks)
                daftar['Tahun Terbit'].pop(indeks)
                print('Data telah dihapus!')
                buku_perpus(daftar_buku_perpus)
                menu_4(daftar)
                
    elif pilihan == '2':
        yakin = yakinkah()
        menu_utama()
    
menu_utama()
