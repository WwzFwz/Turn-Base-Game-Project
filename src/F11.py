from src.validation import input_untill_range_valid
from src.validation import is_range_valid  
from src.validation  import is_all_same_type
from src.validation  import input_untill_type_valid, get_index_by_id

def update_inventory_by_id(general_inventory,user_inventory,user_id:int) :
    # I.S general_inventory dari database(general_inventory), user_inventory telah update
    # F.S Jika user_id  terdapat pada general_inventory, maka row pada user_id akan diupdate dengan data user_inventory
    #     jika tidak maka akan menambahkan row baru dari row data user_inventory
    for j in range(1,len(user_inventory)) :
        found = False
        user_row = user_inventory[j] 
        for i in range(1,len(general_inventory)) :
            general_row = general_inventory[i]
            if (general_row[0] == user_id) and (general_row[1] == user_row[0]) :
                general_inventory[i] = [user_id] + user_row   
                found = True
                break
        if not found : 
            new_data = [user_id] + user_row
            general_inventory.append(new_data)

def get_user_inventory(inventory,user_id:int) :
    # Fungsi menngeluarkan output data user dari database inventory yang memiliki user_id
    user_inventory = [inventory[0][1:]]     
    for row in inventory[1:] :
        if str(row[0]) == str(user_id) :
            user_inventory.append(row[1:])
    return user_inventory  

def get_monster_name(user_monster_inventory,table_monster) :
    # Fungsi untuk mendapatkan nama monster yang terdapat pada user_monster_inventory ,  nama monster diambil dari table_monster
    monster_names = ["Monster Names : "] 
    for i in range(1,len(user_monster_inventory)) : 
        id_monster = user_monster_inventory[i][0]
        found = False
        j = 0 
        while not found and j < len(table_monster): 
            if id_monster == table_monster[j][0] :
                monster_name = table_monster[j][1]
                monster_names.append(monster_name)
                found = True 
                break
            j+=1
    return monster_names


def print_monster_list(user_monsters,monster_names) : # Procedure cetak monster list
    print("============ MONSTER LIST ============")
    for i in range(1,len(user_monsters)) :
        print(f"{i}. {monster_names[i]} (Level : {user_monsters[i][1]})")
    print()

def print_upgrade_price (upgrade_prices) : # Procedure cetak harga upgrade level
    for i in range(4):
        print(f"Level {i+1} -> Level{i+2} : {upgrade_prices[i]}")
    print()
    
def upgrading_monster(monster_level:int,monster_name:str,oc:int,upgrade_prices) :     
    # I.S monster level belum terupgrade atau sudah maksimum (level 5)
    # F.S Jika awalnya monster level belum max maka monster level terupgrade sampai keinginan user dengan level maks,yaitu level 5
    while True  :
        upgrade_price = upgrade_prices[monster_level-1]
        if monster_level == 5 :
            print(f"Level {monster_name} sudah maksimal")
            break
        if upgrade_price > oc :
            print("OC anda tidak cukup")
            break   

        print(f"{monster_name} akan di upgrade ke level {monster_level+1}")
        print(f"Harga untuk melakukan upgrade adalah {upgrade_price}")
        next_upgrade = str(input("Lanjutkan upgrade (y/n) : ")).lower()
        if next_upgrade.lower() =="y" :
            oc -= int(upgrade_price)
            monster_level += 1
            print(f"Selamat, {monster_name} berhasil diupgrade menjadi level {monster_level}")
            next_upgrade = str(input("Lanjutkan upgrade (y/n) : ")).lower()
            if next_upgrade.lower() == "n" :
                print("Upgrade selesai")
                break
            elif next_upgrade.lower() != "y" and next_upgrade.lower() != "n":
                print("error,input salahh")
                break

        elif next_upgrade =="n" :
            print("Upgrade dibatalkan")
            break
        else:
            print("erorr, input salah")
            break
        
    return monster_level,oc
def laboratory(database,user_id,user_role) :  # Program Utama 
    if user_role.lower() != "agent" : # cek role
        return print("Anda bukan agent")
    # Pengambilan data
    monster_inventory = database["monster_inventory"]  
    monster = database["monster"]
    user = database["user"]
    index_user =  get_index_by_id(user_id,user) # index letak data user di database user
    oc = user[index_user][4] # oc yang dimiliki user
    upgrade_prices = [300,500,800,1000] #hardcode harga upgrade 

    
    user_monsters = get_user_inventory(monster_inventory,user_id) # inventory item user
    monster_names = get_monster_name(user_monsters,monster) # nama monster user, terurut sesuai pada user monsters inventory

    print("SELAMAT DATANG DI LAB DR ASEP")
    isLaboratoring = True 
    while isLaboratoring :
        print_monster_list(user_monsters,monster_names) # monster list name ebrdasarkan database monster
        print_upgrade_price(upgrade_prices) # harga upgrade tiap upgrde level
        banyak_monster = len(monster_names)-1
        index_monster = int(input(f"Pilih monster (1 - {banyak_monster}) : "))
        # check apakah user telah memasukkan pilihan monster yang benar sesuai user monsters dan check apakah masukan user merupakan integer
        while not is_range_valid(str(index_monster),banyak_monster+1) or not is_all_same_type(str(index_monster),check_integer=True): 
            index_monster = input_untill_type_valid(str(index_monster), message="Input harus berupa integer",type="integer")
            index_monster= input_untill_range_valid(index_monster,len(monster_names),f"Range pilihan tidak valid \nPilih monster (1-{len(monster_names)-1}: )")
        index_monster = int(index_monster)
        monster_level = user_monsters[index_monster][1]
        monster_name = monster_names[index_monster]
        monster_level,oc = upgrading_monster(int(monster_level),monster_name,int(oc),upgrade_prices)  # akan mengupgrade monster
        user_monsters[index_monster][1] = monster_level # update level monster pada user monsters(inventory)
        next_monster = str(input("Ingin mengupgrade monster lain (y/n)?")).lower()
        if next_monster == "n" : 
            user[index_user][4] = oc
            update_inventory_by_id(monster_inventory,user_monsters,user_id) # update database monster inventory general dengan user inventory
            isLaboratoring = False
