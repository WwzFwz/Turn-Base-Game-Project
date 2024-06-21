from src.F11 import get_user_inventory
from src.F11 import update_inventory_by_id
from src.F12 import merge_tables_by_id
from src.F12 import generate_id_potion
from src.validation import get_index_by_id,is_all_same_type
from src.F13 import table_interface

def beli(objek:str,data_shop,user_inventory,user_data,menu) :   
      # Procedure , I.S user_inventory,oc diambil dari database . F.S penambahan pada user_inventory dan pengurangan OC berdasarkan pembelian user
        oc = user_data[4]
        print(f"Jumlah O.W.C.A Coin mu sekarang {oc}\n")
        could_purchase = True
        id = str(input(f"Masukkan id {objek} : "))
        index_in_shop = get_index_by_id(id,menu) 
        if objek == "potion" :
            index_in_inventory = get_index_by_id(id,generate_id_potion(user_inventory))
        elif objek == "monster" :
            index_in_inventory = get_index_by_id(id,user_inventory)
        else :
            print("Fitur belum ada")
            could_purchase = False    
        if index_in_shop == -999 :      # i == -999 berarti index tidak ada 
            print(f"{objek} tidak terdapat pada shop")
            could_purchase = False   
        elif index_in_inventory != -999 and objek =="monster":
            print(f"Monster {menu[index_in_shop][1]} sudah terdapat di inventory")
            could_purchase = False
        if could_purchase : # purchase objek (kondisi telah tervalidasi)
            stock = int(data_shop[index_in_shop][1])
            price = int(data_shop[index_in_shop][2])
            purchase = 1
            if objek == "potion":
                purchase = str(input("Mau beli berapa banyak potion? : "))
                while not is_all_same_type(input=purchase,check_integer=True) :
                    print("Input Tidak Valid, Masukkan Bilangan Bulat")
                    purchase = str(input("Mau beli berapa banyak potion? : "))
            purchase = int(purchase)
            total_price = price * purchase 
            if purchase > stock :
                print("Stock tidak cukup")
            elif total_price > oc :
                print("Saldo oc tidak cukup")
            else : # stock tersedia dan saldo cukup 
                user_data[4] -= total_price
                data_shop[index_in_shop][1] = stock-purchase
                print(data_shop)
                nama_objek = menu[index_in_shop][1]
                print(f"{objek} {nama_objek} berhasil di beli dengan harga {total_price}")
                if objek == "monster" :
                    user_inventory.append([id,purchase])
                elif (objek == "potion" and index_in_inventory == -999):
                    user_inventory.append([nama_objek,purchase])
                else : #objek =="potion" dan potion ada di inventory
                    current_amount = user_inventory[index_in_inventory][1]
                    new_amount = purchase + int(current_amount)
                    user_inventory[index_in_inventory][1] = new_amount
                    


def shop(database,user_id,user_role) :  # Program Utama
    # Inisialisasi data dari database
    user = database["user"]
    monster = database["monster"]
    monster_shop = database["monster_shop"]
    monster_inventory = database["monster_inventory"]
    item_shop = database["item_shop"]
    item_inventory = database["item_inventory"]
    user_items = get_user_inventory(item_inventory,user_id)
    user_monsters = get_user_inventory(monster_inventory,user_id)   

    if user_role.lower() != "agent" : 
        return print("Ini shop untuk role agent")
    index_user = get_index_by_id(user_id,user)
    user_data = user[index_user]
    print("Selamat datang di indoseptember, Selamat belanja :) \n")
    is_Shopping =  True 
    while is_Shopping :
        menu_potion = generate_id_potion(item_shop)
        menu_monster = merge_tables_by_id(monster,monster_shop)
        aksi = str(input("Pilih aksi (lihat/beli/keluar) \n:")).lower()
        if aksi != "lihat" and aksi != "beli" and  aksi != "keluar" :   # cek input 
            print("Aksi yang anda berikan tidak valid, silahkan input lagi ")
        elif aksi == "lihat" :
            objek = str(input(("Mau lihat apa (monster/potion) : ") )).lower()                                                          
            if objek == "monster" :
                table_interface(menu_monster,"SHOP MONSTER KOSONG")    
            elif objek == "potion" :
                table_interface(menu_potion,"SHOP POTION KOSONG")
            else :
                print("Input tidak valid")

        elif aksi == "beli" :
            objek = str(input(("Mau beli apa (monster/potion) :"))).lower()
            if objek == "monster" :
                beli(objek="monster",data_shop=monster_shop,user_inventory=user_monsters,user_data=user_data,menu=menu_monster)
                update_inventory_by_id(monster_inventory,user_monsters,user_id)    # perbarui database monster_inventory
            elif objek == "potion" :
                beli(objek="potion",data_shop=item_shop,user_inventory=user_items,user_data=user_data,menu=menu_potion)  
                update_inventory_by_id(item_inventory,user_items,user_id) # perbarui database item_inventory
            else : 
                print("Hanya terdapat shop potion dan monster ")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
        elif aksi == "keluar":
            is_Shopping = False
            print("Terimakasih sudah berbelanja")
        else : 
            print('Fitur belum ada')
        user[index_user] =user_data #update oc
