from tabulate import tabulate
import pyinputplus as pyip

menu = ['1. Tampilkan Daftar Mobil',
        '2. Tambahkan Daftar Mobil Disewa',
        '3. Hapus Daftar Mobil Disewa',
        '4. Ubah Data Mobil Disewa',
        '5. Exit']

read_menu = ['1. Tampilkan Seluruh Daftar Mobil',
             '2. Tampilkan Daftar Mobil yang Dicari',
             '3. Urutkan Daftar Harga Mobil',
             '4. Kembali ke Menu Utama']

create_menu = ['1. Tambah Daftar Mobil',
               '2. Kembali ke Menu Utama']

model_toyota = ['Avanza',
                'Innova',
                'Rush',
                'Yaris',
                'Agya']

model_honda = ['Jazz',
               'BR-V',
               'Mobilio',
               'Brio',
               'City']

delete_menu = ['1. Hapus Daftar Mobil',
               '2. Kembali ke Menu Utama']

update_menu = ['1. Ubah Data Keseluruhan Mobil',
               '2. Ubah Data Kategori Tertentu',
               '3. Kembali ke Menu Utama']


stockMobil = [
    {'carId':'TOAVMA14', 'merk':'Toyota', 'model': 'Avanza', 'transmisi':'Manual', 'tahun': 2014, 'harga': 300000, 'stock': 5},
    {'carId':'HOJAAU20', 'merk':'Honda', 'model': 'Jazz', 'transmisi':'Automatic', 'tahun': 2020, 'harga':500000, 'stock': 4},
    {'carId':'TOINMA16', 'merk':'Toyota', 'model': 'Innova', 'transmisi':'Manual', 'tahun': 2016, 'harga':400000, 'stock': 4}
    ]
headers = ["Car Id", "Merk Mobil", "Model Mobil", "Transmisi Mobil", "Tahun", "Harga Per hari", "Stock Mobil"]

t_stockMobil = tabulate([(mobil['carId'], mobil['merk'], mobil['model'], mobil['transmisi'], mobil['tahun'], mobil['harga'], mobil['stock']) for mobil in stockMobil], headers, tablefmt='grid')


def generate_table(data) :
    return tabulate([(mobil['carId'], mobil['merk'], mobil['model'], mobil['transmisi'], mobil['tahun'], mobil['harga'], mobil['stock']) for mobil in stockMobil], headers, tablefmt='grid')  


### Read Data Function ###
def read_data() :
    while True :
        print("\n===Sub Menu Read Data Bay's Rent Cars===")
        for i in read_menu :
            print (i)
        read = pyip.inputNum(prompt="\nSilahkan pilih Sub Menu Read Data [1-4]: ", min=1, max=4)
        if read == 1 :
            print("\nBerikut merupakan seluruh daftar stock mobil yang tersedia :\n{}".format(t_stockMobil))
        elif read == 2 :
            print(t_stockMobil)
            carId_choice = pyip.inputMenu(prompt="Masukkan Car Id yang ingin dilihat:\n", choices=[car['carId'] for car in stockMobil], numbered=True)
            filtered_car = [car for car in stockMobil if car['carId'] == carId_choice]
            if filtered_car :
                filtered_table = tabulate([(mobil['carId'], mobil['merk'], mobil['model'], mobil['transmisi'], mobil['tahun'], mobil['harga'], mobil['stock']) for mobil in filtered_car], headers, tablefmt='grid')
            print("\nBerikut merupakan detail mobil dengan Car Id {}:\n{}".format(carId_choice, filtered_table))
        elif read == 3 :
            sort = pyip.inputMenu(prompt="\nUrutkan berdasarkan sewa :\n", choices=['Termahal', 'Termurah'], numbered=True)
            if sort == 'Termahal' :
                sorted_stockMobil = sorted(stockMobil, key = lambda car: car['harga'], reverse=True)
                t_sorted_stockMobil = tabulate([(mobil['carId'], mobil['merk'], mobil['model'], mobil['transmisi'], mobil['tahun'], mobil['harga'], mobil['stock']) for mobil in sorted_stockMobil], headers, tablefmt='grid')
                print("\nBerikut merupakan daftar mobil berdasarkan harga sewa termahal :\n{}".format(t_sorted_stockMobil))
            else :
                sorted_stockMobil = sorted(stockMobil, key = lambda car: car['harga'], reverse=False)
                t_sorted_stockMobil = tabulate([(mobil['carId'], mobil['merk'], mobil['model'], mobil['transmisi'], mobil['tahun'], mobil['harga'], mobil['stock']) for mobil in sorted_stockMobil], headers, tablefmt='grid')
                print("\nBerikut merupakan daftar mobil berdasarkan harga sewa termurah :\n{}".format(t_sorted_stockMobil))               
        else :
            mainMenu()

### Create Data Function ###
def create_data() :
    global t_stockMobil
    while True :
        print("\n===Sub Menu Create Data Bay's Rent Cars===")
        for i in create_menu :
            print (i)
        create = pyip.inputNum(prompt="\nSilahkan pilih Sub Menu Create Data [1-2]: ", min=1, max=2)
        if create == 1 :
            addMerk = pyip.inputMenu(prompt="Masukkan merk mobil :\n", choices=['Toyota','Honda'], numbered=True)
            if addMerk == 'Toyota' :
                addModel = pyip.inputMenu(prompt="Masukkan model mobil :\n", choices=[m for m in model_toyota], numbered=True)
            elif addMerk == 'Honda' :
                addModel = pyip.inputMenu(prompt="Masukkan model mobil :\n", choices=[m for m in model_honda], numbered=True)
            addTransmisi = pyip.inputMenu(prompt="Masukkan transmisi mobil :\n", choices=['Manual','Automatic'], numbered=True)
            addTahun = pyip.inputNum(prompt="Masukkan tahun mobil [2010-2020] : ", min=2010, max=2020)
            addHarga = pyip.inputNum(prompt="Masukkan harga sewa harian [300000-1000000] : ", min=300000, max=1000000)
            addStock = pyip.inputNum(prompt="Masukkan stock jumlah mobil [1-10] : ", min=1, max=10)
            addCarId = addMerk[0:2].upper()+addModel[0:2].upper()+addTransmisi[0:2].upper()+str(addTahun)[-2:]            
            addValidation = pyip.inputChoice(prompt="Yakin untuk menambahkan mobil ? [Y/N] ", choices=['Y', 'N']).upper()
            if addValidation == 'Y' : 
                car_exists = False
                for car in stockMobil:
                    if car['carId'] == addCarId:
                        car['harga'] = addHarga
                        car['stock'] = addStock
                        t_stockMobil = generate_table(stockMobil)
                        print("\nMobil dengan CarId yang sama sudah ada dalam daftar. Mengupdate data mobil.")
                        print(t_stockMobil)
                        car_exists = True
                        break
                if not car_exists:
                    stockMobil.append({'carId': addCarId, 'merk': addMerk, 'model': addModel, 'transmisi': addTransmisi, 'tahun': addTahun, 'harga': addHarga, 'stock': addStock})
                    t_stockMobil = generate_table(stockMobil)
                    print("\nMobil baru berhasil ditambahkan ke daftar!")
                    print(t_stockMobil)
            else :
                print("\nMobil gagal untuk ditambahkan!")
        else :
            mainMenu()

### Delete Data Function ###
def delete_data() :
    global t_stockMobil
    while True :
        print("\n===Sub Menu Delete Data Bay's Rent Cars===")
        for i in delete_menu :
            print (i)
        delete = pyip.inputNum(prompt="\nSilahkan pilih Sub Menu Delete Data [1-2]: ", min=1, max=2)
        if delete == 1 :
            print(t_stockMobil)
            deleteCarId = pyip.inputMenu(prompt="Masukkan Car Id yang akan dihapus :\n", choices=[car['carId'] for car in stockMobil], numbered=True)
            deleteValidation = pyip.inputChoice(prompt="Yakin untuk menghapus mobil? [Y/N] ", choices=['Y', 'N']).upper()
            if deleteValidation == 'Y':
                for car in stockMobil:
                    if car['carId'] == deleteCarId:
                        index_to_delete = stockMobil.index(car)
                        del stockMobil[index_to_delete]
                        break
                t_stockMobil = generate_table(stockMobil)
                print("\nMobil berhasil dihapus dari daftar!")
                print(t_stockMobil)
            else:
                print("\nPenghapusan mobil dibatalkan!")
        else :
            mainMenu()

### Update Data Function ###
def update_data() :
    global t_stockMobil
    while True :
        print("\n===Sub Menu Update Data Bay's Rent Cars===")
        for i in update_menu :
            print (i)
        update = pyip.inputNum("\nSilahkan pilih Sub Menu Update Data [1-3]: ", min=1, max=3)
        if update == 1 :
            print(f"\n{t_stockMobil}")
            changeCarId = pyip.inputMenu(prompt="Masukkan Car Id yang akan diubah :\n", choices=[car['carId'] for car in stockMobil], numbered=True)
            for car in stockMobil:
                    if car['carId'] == changeCarId :
                        updateIndex = stockMobil.index(car)
                        break
            updateValidation = pyip.inputChoice(prompt="Yakin untuk mengubah keseluruhan data mobil ini ? [Y/N] ", choices=['Y', 'N']).upper()
            if updateValidation == 'Y':
                updateMerk = pyip.inputMenu(prompt="Masukkan merk mobil baru :\n", choices=['Toyota','Honda'], numbered=True)
                if updateMerk == 'Toyota' :
                    updateModel = pyip.inputMenu(prompt="Masukkan model mobil baru :\n", choices=[m for m in model_toyota], numbered=True)
                elif updateMerk == 'Honda' :
                    updateModel = pyip.inputMenu(prompt="Masukkan model mobil baru :\n", choices=[m for m in model_honda], numbered=True)
                updateTransmisi = pyip.inputMenu(prompt="Masukkan transmisi mobil baru :\n", choices=['Manual','Automatic'], numbered=True)
                updateTahun = pyip.inputNum(prompt="Masukkan tahun mobil baru [2010-2020] : ", min=2010, max=2020)
                updateHarga = pyip.inputNum(prompt="Masukkan harga sewa harian baru [300000-1000000] : ", min=300000, max=1000000)
                updateStock = pyip.inputNum(prompt="Masukkan stock jumlah mobil baru [1-10] : ", min=1, max=10)
                updateCarId = updateMerk[0:2].upper()+updateModel[0:2].upper()+updateTransmisi[0:2].upper()+str(updateTahun)[-2:]
                stockMobil[updateIndex] = {'carId': updateCarId, 'merk': updateMerk, 'model': updateModel, 'transmisi': updateTransmisi, 'tahun': updateTahun, 'harga': updateHarga, 'stock':updateStock}
                t_stockMobil = generate_table(stockMobil)
                print("\nData mobil berhasil diubah dari daftar!")
                print(t_stockMobil)
            else :
                print("\nPerubahan data mobil dibatalkan!")
        elif update == 2 :
            print(f"\n{t_stockMobil}")
            changeCarId = pyip.inputMenu(prompt="Masukkan Car Id yang akan diubah :\n", choices=[car['carId'] for car in stockMobil], numbered=True)
            for car in stockMobil:
                    if car['carId'] == changeCarId :
                        updateIndex = stockMobil.index(car)
                        break
            updateCategory = pyip.inputMenu(prompt="\nMasukkan Kategori Data yang akan diubah :\n", choices = ["Merk Mobil", "Model Mobil", "Transmisi Mobil", "Tahun", "Harga Per hari", "Stock Mobil"], numbered=True)
            if updateCategory == "Merk Mobil":
                keyChange = 'merk'
                newMerk = pyip.inputMenu(prompt="Masukkan merk mobil baru :\n", choices=['Toyota','Honda'], numbered=True)
                stockMobil[updateIndex][keyChange]=newMerk
                t_stockMobil = generate_table(stockMobil)                
                print(t_stockMobil)
                print("Perubahan data merk berhasil!")
            elif updateCategory == "Model Mobil":
                keyChange = 'model'
                if stockMobil[updateIndex]['merk'] == 'Toyota' :
                    newModel = pyip.inputMenu(prompt="Masukkan model mobil baru :\n", choices=[m for m in model_toyota], numbered=True)
                elif stockMobil[updateIndex]['merk'] == 'Honda' :
                    newModel = pyip.inputMenu(prompt="Masukkan model mobil baru :\n", choices=[m for m in model_honda], numbered=True)
                stockMobil[updateIndex][keyChange]=newModel
                t_stockMobil = generate_table(stockMobil)
                print(t_stockMobil)
                print("Perubahan data model berhasil! ")
            elif updateCategory == "Transmisi Mobil":
                keyChange = 'transmisi'
                newTransmisi = pyip.inputMenu(prompt="Masukkan transmisi mobil baru :\n", choices=['Manual','Automatic'], numbered=True)
                stockMobil[updateIndex][keyChange]=newTransmisi
                t_stockMobil = generate_table(stockMobil)
                print(t_stockMobil)
                print("Perubahan data transmisi berhasil!")               
            elif updateCategory == "Tahun":
                keyChange = 'tahun'
                newTahun = pyip.inputNum(prompt="Masukkan tahun mobil baru [2010-2020] : ", min=2010, max=2020)
                stockMobil[updateIndex][keyChange]=newTahun
                t_stockMobil = generate_table(stockMobil)
                print(t_stockMobil)
                print("Perubahan data tahun berhasil!")
            elif updateCategory == "Harga Per hari":
                keyChange = 'harga'
                newHarga = pyip.inputNum(prompt="Masukkan harga sewa harian baru [300000-1000000] : ", min=300000, max=1000000)
                stockMobil[updateIndex][keyChange]=newHarga
                t_stockMobil = generate_table(stockMobil)
                print(t_stockMobil)
                print("Perubahan data harga berhasil!")                   
            elif updateCategory == "Stock Mobil":
                keyChange = 'stock'
                newStock = pyip.inputNum(prompt="Masukkan stock jumlah mobil baru [1-10] : ", min=1, max=10)
                stockMobil[updateIndex][keyChange]=newStock
                t_stockMobil = generate_table(stockMobil)
                print(t_stockMobil)
                print("Perubahan data stock berhasil!")   
        else :
            mainMenu()

### Main Menu Function ###
def mainMenu() :
    while True :
        print("\n=====Menu Utama Bay's Rent Cars=====")
        for i in menu :
            print(i)
        pilihan = pyip.inputNum(prompt="\nSilahkan pilih menu utama [1-5]: ", min=1, max=5)
        if pilihan == 1 :
            read_data()
        elif pilihan == 2 :
            create_data()
        elif pilihan == 3 :
            delete_data()
        elif pilihan == 4 :
            update_data()
        else :
            print("\nTerima kasih dan Selamat Tinggal !")
            quit()

mainMenu()