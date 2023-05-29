tampungAntrian = [
    # {0: 1},
    # {0: 2},
    # {0: 3},
    # {0: 4},
    # {1: 1},
    # {1: 2},
    # {1: 3},
    # {2: 1},
    # {2: 2},
    # {2: 3},
    # {3: 1},
    # {3: 2},
]


menuTersedia = ['POLI UMUM', 'POLI GIGI', 'POLI ANAK', 'POLI JANTUNG']


def antrianByMenu(index):
    allAntrian = []
    for antrian in tampungAntrian:
        for key, values in antrian.items():

            if (key == index):
                allAntrian.append(values)
    return allAntrian


def cekAntrian(index):
    allAntrian = antrianByMenu(index)

    antrianAnda = len(allAntrian)+1 if len(allAntrian) > 0 else 1

    # print(allAntrian)
    # print(antrianAnda)
    # return False
    pushAntrian(index, antrianAnda)

    return [
        {'antrianSeluruhnya': allAntrian},
        {'antrianAnda': antrianAnda}
    ]


def pushAntrian(indexMenu, antrian):
    data = {indexMenu: antrian}
    tampungAntrian.append(data)


def deleteData(index):
    antrianTerdepan = antrianByMenu(index)

    if (len(antrianTerdepan) <= 0):
        print('Data pada {} masing kosong'.format(menuTersedia[index]))

    else:
        for antrian in tampungAntrian:
            for key, values in list(antrian.items()):

                if (values == antrianTerdepan[0]):
                    antrian.pop(key, antrianTerdepan[0])

        print('Nomor antrian {} berhasil dihapus'.format(menuTersedia[index]))
        if len(antrianByMenu(index)) > 0:
            tampilAntrian(index)
        else:
            print("Tidak ada antrian yang tersedia")

    print("\n")
    next(index)


def tambahAntrian(index):

    antrianByMenu = cekAntrian(index)
    antrianSeluruhnya = antrianByMenu[0]['antrianSeluruhnya']
    antrianAnda = antrianByMenu[1]['antrianAnda']

    print("\nAntrian ke {} berhasil ditambahkan".format(menuTersedia[index]))

    print("\nBerikut nomor antrian Anda : ", antrianAnda)

    if (len(antrianSeluruhnya) > 0):
        print("Antrian saat ini : ", antrianSeluruhnya[0])

    next(index)


def tampilAntrian(index):
    antrianPoli = antrianByMenu(index)
    if len(antrianPoli) > 0:
        print("Berikut list antrian dari ", menuTersedia[index])
        for antrian in antrianPoli:
            print(antrian, end=" ")
        print("\n")
    else:
        print('Data pada {} masing kosong'.format(menuTersedia[index]))

    next(index)


def antrianSaatIniByPoli(index):
    allAntrian = antrianByMenu(index)
    if len(allAntrian) > 0:
        print('Nomor antrian yang sedang berlangsung yakni : ', allAntrian[0])
    else:
        print('Data pada {} masing kosong'.format(menuTersedia[index]))
    print("\n")

    next(index)


def next(indexMenu):
    currMenu = menuTersedia[indexMenu]

    print("\n===== KELOLA DATA {} =====".format(currMenu))
    print("1. Tambah Data")
    print("2. Tampil Data")
    print("3. Cek Antrian saat ini")
    print("4. Hapus Data")
    print("5. Kembali ke menu")

    pilih = input('Masukkan pilihan Anda : ')

    match(pilih):
        case '1':
            tambahAntrian(indexMenu)

        case '2':
            tampilAntrian(indexMenu)
        case '3':
            antrianSaatIniByPoli(indexMenu)
        case '4':
            deleteData(indexMenu)
        case '5':
            start()
            print(tampungAntrian)

        case _:
            print('\npilihan tidak tersedia')
            next(indexMenu)


def start():

    print('\nSilahkan pilih poli dari menu yang tersedia \n')

    for (i, menu) in enumerate(menuTersedia):
        print("{}. {}".format(i+1, menu))

    print("{}. Keluar Program".format(len(menuTersedia)+1))
    pilihanMenu = int(input('\ninput angka dari menu yang tersedia : '))

    if (pilihanMenu == len(menuTersedia)+1):
        exit()
    else:
        indexMenu = pilihanMenu - 1

        if (pilihanMenu < 0 or pilihanMenu > len(menuTersedia)):
            print('\nMenu tidak tersedia')

        else:
            next(indexMenu)
        # print(tampungAntrian)


start()
