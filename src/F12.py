from src.validation import *



def filter_table_by_id(table1, table2):
    new_table = []
    new_table.append(table1[0])
    for i in range(1,len(table1)):  # Mulai dari baris kedua
        elemen_exist = False
        for j in range(1, len(table2)):  # Mulai dari baris kedua
            if table1[i][0] == table2[j][0]:
                elemen_exist = True
                break
    
        if  not elemen_exist:
            new_table.append(table1[i]) 
    return new_table

def table_interface(table,message):
    # Cari panjang maks tiap kolom
    column_length = []
    if len(table) == 1 :    
        print(message)
    else :
        for col in range(len(table[0])):
            max_column_length = max(len(str(row[col])) for row in table)
            column_length.append(max_column_length)
        # Cetak tabel
        for row in table:
            for i in range(len(row)):
                item = row[i]
                kol = column_length[i]
                print(" "+ str(item) + " " * (kol - len(str(item))+1) + "|", end="")
            print()
def merge_tables_by_id(table1,table2) :
    header = table1[0] + table2[0][1:]
    merged_table = [header]

    for row1 in table1[1:]:
        id1 = row1[0]
        for row2 in table2[1:]:
            id2 = row2[0]
            if id1 == id2:
                merged_table.append(row1 + row2[1:])
                break
    return merged_table
def generate_id_potion(table_potion) :
    new_table = [["ID"] + table_potion[0]]
    i = 1
    for row in table_potion[1:] :
        new_table.append([str(i)] + row)
        i +=1
    return new_table


def delete_row(indeks:int,table) :      
    indeks_maks = len(table)-1
    if indeks_maks < indeks  or indeks < 0 :
        print("indeks tidak valid")
        return table
    else :               
        new_table = []
        for i in range(indeks_maks+1):
            if i != indeks:
                new_table.append(table[i])
        return new_table 
    
def input_data(objek:str,status_input:str,shop_data) ->int :
    stock,harga = "0","0"  # status_input == hapus 
    id = str(input((f"Masukkan id {objek} : ")))  # Pada potion masukkan type
    while (get_index_by_id(id,shop_data) == -999) :
        id = str(input((f"Id tidak terdapat pada shop \n Masukkan id {objek} : "))) 
            
    if status_input != "hapus" :
        stock = str(input(f"Masukkan stok {status_input} : "))
    while not is_all_same_type(stock,check_integer=True) or not is_range_valid(stock,99999) :
        stock = input_untill_type_valid(stock,f"Masukkan stock {status_input} :",type="integer")
        stock = input_untill_range_valid(stock,99999,f"Input Tidak Valid, stock harus >= 0\nMasukkan stok{status_input} :")
    if status_input != "hapus" :
        harga = str(input(f"Masukkan harga {status_input} : "))
    while not is_all_same_type(harga,check_integer=True)  or not is_range_valid(harga,99999) :
        harga = input_untill_type_valid(harga,message=f"Masukkan harga {status_input} : ",type="integer")
        harga = input_untill_range_valid(harga,99999,message=f"Input Tidak Valid, Harga harus >= 0\nMasukkan harga {status_input :}")
    return int(stock),int(harga),str(id)
                                         
def shop_management(database,user_role) :
    monster = database['monster']
    monster_shop = database['monster_shop']
    item_shop = database['item_shop']
    if user_role.lower() != "admin" :  # cek akses
        print("Anda tidak memiliki akses ke shop management")
        return monster_shop,item_shop
    
    isManaging = True
    while  isManaging : 

        menu_monsters = merge_tables_by_id(monster,monster_shop)
        menu_items = generate_id_potion(item_shop)
        aksi = str(input("Pilih aksi(lihat/tambah/ubah/hapus/keluar) :")).lower()
        if aksi == "lihat" :
            objek = str(input(f"Mau {aksi} apa?(monster/potion)?")).lower()
            if objek  == "monster" :
                table_interface(menu_monsters,"TIDAK ADA MONSTER DI DALAM SHOP")
            elif objek == "potion" :
                table_interface(menu_items,"TIDAK ADA POTION DI DALAM SHOP")
            else :
                print("Input salah")
        elif aksi.lower() == "tambah" :
            objek = str(input(f"Mau {aksi} apa?(monster/potion)?")).lower()
            if objek == "monster"  :
                not_added = filter_table_by_id(monster,monster_shop)
                if len(not_added) == 1 :
                    print("Semua jenis monster telah ada di di shop")
                else :
                    table_interface(not_added,"")
                    stock,harga,id_monster = input_data(objek,"awal",not_added)
                    monster_shop.append([int(id_monster),stock,harga])
                    
            elif objek == "potion" :
                potion = [["type"],["strength"],["resilience"],["healing"]]     #jenis potion hardcode
                not_added= (filter_table_by_id(potion,item_shop))
                id_not_added = generate_id_potion(not_added)
                if len(not_added) == 1 :
                    print("Semua jenis potion telah ada di shop")
                else : 
                    table_interface(id_not_added,"") 
                    stock ,harga ,id_potion = input_data(objek,"awal",not_added)
                    item_shop.append([id_potion,stock,harga])
            else :
                print("input tidak valid")
        elif aksi =="ubah" :
            objek = str(input(f"Mau {aksi} apa?(monster/potion)?")).lower() 
            if objek == "monster" :
                if len(monster_shop) == 1 :
                    print("Belum terdapat monster apapun pada monster shop, silahkan tambahkan terlebih dahulu pada fitur tambah")
                else :
                    stock ,harga ,id_monster = input_data(objek,"baru",menu_monsters)
                    index_monster = get_index_by_id(id_monster,monster_shop)
                    monster_shop[index_monster] = [id_monster,stock,harga]

            elif objek == "potion" :
                if len(item_shop) == 1  :
                    print("Belum terdapat potion apapun pada potion shop, silahkan tambahkan terlebih dahulu pada fitur tambah")
                else :
                    stock,harga, id_potion = input_data(objek,"baru",menu_items)
                    index_potion = id_potion
                    item_shop[index_potion][1] = stock
                    item_shop[index_potion][2] = harga 

            else :
                print("input salah")
        elif aksi == "hapus" :
            objek = str(input("Mau hapus apa min ? (monster/potion?)")).lower()
            if objek == "monster" :
                if len(monster_shop) == 1 :
                    print("MONSTER PADA SHOP MONSTER TELAH KOSONG")
                else : 
                    table_interface(menu_monsters,"")

                    _,_,id_monster = input_data(objek,"hapus",menu_monsters)
                    yakin = str(input("Yakin mengubah (y/n) ")).lower()
                    if yakin == "y"  : 
                        index_monster = get_index_by_id(id_monster,monster_shop)
                        monster_shop=delete_row(index_monster,monster_shop)
                    elif yakin == "n" :
                        print("Tidak jadi mengubah")
                    else :
                        print("input salah")

            elif objek == "potion" :
                if len(item_shop) == 1 :
                    print("POTION PADA SHOP POTION TELAH KOSONG")
                else : 
                    table_interface(menu_items, "POTION PADA SHOP POTION TELAH KOSONG")
                    _,_,id_potion = input_data(objek,"hapus",menu_items)
                    yakin = str(input("Yakin mengubah (y/n) ")).lower()
                    if yakin == "y"   :
                        print(item_shop)
                        item_shop = delete_row(int(id_potion),item_shop)
                        print(item_shop)
                        
                    else :
                        print("Tidak jadi mengubah")

            else : 
                print("input salah")
        elif aksi == "keluar" :
            isManaging = False
            print("terimakasih")
        else :
            print("Fitur belum ada")
    return monster_shop,item_shop
    
    
