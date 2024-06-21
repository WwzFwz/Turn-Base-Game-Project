from src.F11 import get_user_inventory
from src.validation import get_index_by_id,is_all_same_type
from src.F00 import randomNumberGenerator
from src.F05 import graphics
from src.F12 import merge_tables_by_id
from src.F05 import damage_dealt,damage_taken
from src.F07 import level_calculation 
from src.F11 import update_inventory_by_id
import time

def MonsterBall (enemy_array:list)->bool:
    # monsterball
    success = False
    level = enemy_array[5]
    number = randomNumberGenerator(0,100)
    if(level == 1):
        if(number <= 75):
            success = True
    if(level == 2):
        if(number <= 50):
            success = True 
    if(level == 3):
        if(number <= 25):
            success = True
    if(level == 4):
        if(number <= 10):
            success = True
    if(level == 5):
        if(number <= 5):
            success = True
    if (success == True):
        print("Swoosshhhhh, Anda mengeluarkan Monster Ball !!!")
        print("Selamat, Anda berhasil mendapatkan Monster",enemy_array[1])
        print("Name         :",enemy_array[1])
        print("ATK Power    :",enemy_array[2])
        print("DEF Power    :",enemy_array[3])
        print("HP           :",enemy_array[4])
        print("Level        :",enemy_array[5])
    else:
        print("Swoosshhhhh, Anda mengeluarkan Monster Ball !!!")
        print("Yahhh, Anda belum berhasil mendapatkan monster Zuko !!!")
    return success

def print_stat_awal(monster:list,graphics:list,text:str) :
    # Procedure mencetak stat monster pada awal battle
    random_index = randomNumberGenerator(0,len(graphics))
    print(graphics[random_index])
    print(text)
    print(f"Monster Type   : {monster[1]}")
    print(f"Attack Power   : {int(monster[2])}",)
    print(f"Defense Power  : {int(monster[3])}",)
    print(f"Monster Health : {int(monster[4])}",)
    print(f"Level : {monster[5]}")
    print("======================================")  
def select_available_monster(user_monsters:list):
    # Fungsi menerima input user_monster(inventory monster yang dimiliki user)
    # Fungsi mengeluarkan output isFigthing bernilai True dan user_monster yang tidak kosong jika invenory monster user tidak kosong
    isFighting = True 
    user_monster = []
    urutan = 1
    print("===========MONSTER LIST===========")
    for i in range(1,len(user_monsters)) :   # printing monster list
        print(f"{urutan}. {user_monsters[i][1]} (level {user_monsters[i][5]}) ")
        urutan +=1
    
    index_monster = str(input("pilih monster :"))
    attempts_id =  10
    while int(index_monster)>=len(user_monsters) or int(index_monster) < 1 or not is_all_same_type(index_monster,check_integer=True): # validating input
        print("Monster tidak ada, Masukan pilihan monster yang ada !")
        index_monster = str(input("pilih monster : "))
        attempts_id -=1
    if attempts_id == 0 :
        isFighting = False
        print("Sepertinya anda belum memiliki monster, silahkan beli di shop terlebih dahulu")
    else :
        user_monster = user_monsters[int(index_monster)]
    
    return isFighting,user_monster
def input_perintah(turns,user_monster) :
    # Fungsi mencetak perintah yang tersedia serta meminta user melakukan pemilihan perintah
    print(f"=============== Turns {turns} ({user_monster[1]})===============")
    print("1. Attack")
    print("2. Use Potion")
    print("3. Monsterball")
    print("4. Quit")
    perintah =  str(input("Pilih perintah : "))
    return perintah

def print_status(turns:int,attacker_monster:list,defender_monster:list,attacker:list) :
    # Procedure mencetak keadaan monster setelah diserang
    if defender_monster[4] <= 0 : # cek hp
        defender_monster[4]= 0
    if attacker == "enemy" :
        print(f"=============== Turns {turns} ({attacker_monster[1]})===============")
    print(f"Monster Type   : {defender_monster[1]}")
    print(f"Attack Power   : {int(defender_monster[2])}",)
    print(f"Defense Power  : {int(defender_monster[3])}",)
    print(f"Monster Health : {int(defender_monster[4])}",)
    print(f"Level : {defender_monster[5]}")
    print("======================================")

def print_potion(user_inventory) : 
    # I.S potion quantity kosong
    # F.S potion quantity terisi kuantitas tiap potion yang dimiliki user
    potion_arr = ["strength","resilience","healing"]
    potion_quantity = []
    for potion in potion_arr :
        found = False
        for row in user_inventory :
            if potion == row[0] :
                potion_quantity.append(row[1])
                found = True
                break
        if not found  :
            potion_quantity.append("0")
    print(f"=================POTION LIST=================")
    print(f"1.Strength Potion (Quantity : {potion_quantity[0]})----Increase ATK Power")
    print(f"2.Resilience Potion (Quantity : {potion_quantity[1]})----Increase DEF power")
    print(f"3.Healing  Potion (Quantity : {potion_quantity[2]})---Restore Health")
    print(f"4.Cancel")
    print("====================================")
            
def random_monster_data(monster,level_monster) :
    # Fungsi mengambil moster lawan secara acak
    index_monster = randomNumberGenerator(1,len(monster)) 
    monster_enemy = monster[index_monster]+ [str(level_monster )]
    return monster_enemy



def duel (battle_status,user_monster,enemy_monster,oc_reward) :
    # I.S battle_status belum diperbarui
    # F.S battle status diperbarui setelah melakukan serangkaian pertarunga
    

    # Player menyerang monster bot terlebih dahulu
    damage_dealth_user = damage_dealt(atk_power=user_monster[2])  # Damage yang diberikan user ke monster bot lawan
    damage_taken_enemy = damage_taken(def_power=enemy_monster[3],damage_dealt=damage_dealth_user) # Damage yang diterima monster bot lawan
    enemy_monster[4] = int(enemy_monster[4]-damage_taken_enemy) # Pengurangan hp bot monster lawan
    print_status(turns=battle_status[0],attacker_monster = user_monster,defender_monster=enemy_monster,attacker="user") # Mencetak status atribut dan hp monster bot setelah diserang
    time.sleep(0.5) # jeda waktu

    # Monster bot kemudian memberikan serangan balasan ke user 
    damage_dealth_enemy = damage_dealt(atk_power=enemy_monster[2]) # Damage yang diberikan monster ke bot lawan
    damage_taken_user = damage_taken(def_power=user_monster[3],damage_dealt=damage_dealth_enemy) # Damage yang diterima monster bot lawan
    user_monster[4] = int(user_monster[4]-damage_taken_user) # Pengurangan hp bot user 

        
    # Mengecek apakah sudah ada monster yang wafat atau belum
    if enemy_monster[4] <= 0 : # User menyerang terlebih dahulu sehingga kemungkinan monster bot wafat lebih dulu
        battle_status[1] = False # Battle berakhir 
        battle_status[2] = True # User menang
        battle_status[5] += oc_reward # Menambahkan hadiah oc
    elif user_monster[4] <= 0 : # Jika monster user telah wafat
        print_status(turns=battle_status[0],attacker_monster=enemy_monster,defender_monster=user_monster,attacker="enemy")
        battle_status[1] = False    # Battle berakhir 
        battle_status[2] = False # User kalah
    else : # Pertarungan belum selesai karena belum ada monster yang wafat
        battle_status[1] = True # Battle masih berlanjut
        battle_status[2] = False # Belum ada Pemenang
        print(f"WHOOOZZZ Monster {enemy_monster[1]} menyerang balik anda")
        print_status(turns=battle_status[0],attacker_monster=enemy_monster,defender_monster=user_monster,attacker="enemy")

    battle_status[0]+= 1 # turns betikutnya
    battle_status[3]+= damage_dealth_user # 
    battle_status[4]+= damage_taken_user

def drink_potion(user_item_inventory,potion_used:list,user_monster:list,hp_max:int) :
    # I.S user_monster masih belum terupdate
    # F.S Stat pada user_monster terupdate jika user menggunakan potion 
    potion_arr = ["strength","resilience","healing"]
    daftar_id = ["1","2","3","4"]
    drink_potion = False
    # pilih potion
    id_potion = str(input("Pilih type : ")) 
    while id_potion not in daftar_id  : # Meminta hingga input id_potion valid
        print("Input salah")
        id_potion = str(input("Pilih potion : ")) 

    if id_potion =="4": # User tidak jadi menggunakan potion
        print("Engga jadi beli")
        cancel = True
        index_potion_in_inventory = -999 # Tidak ada di inventory

    else : # Membaca type potion berdasarkan input [ilihan id ]
        type_potion = potion_arr[int(id_potion)-1] 
        index_potion_in_inventory = get_index_by_id(type_potion,user_item_inventory)
        cancel = False
    # Mengecek apakah potion yang dipilih sudah digunakan
    if not cancel  and (type_potion in potion_used)  :
        cancel = True 
        if type_potion == "strength" :
            print(f"Tadi udah minum jamu kuat")
        elif type_potion =="resilience" :
            print(f"Udah minum resilience bro")
        else : # type_potion == "healing"
            print(f"Tadi udah minum teh healing ini")

    
    # Mengecek apakaah terdpat stock potion yang tersedia jika user memilih untuk menggunaka potion
    if index_potion_in_inventory  != -999 and not cancel:     
        current_stock = int(user_item_inventory[index_potion_in_inventory][1] )
        drink_potion = False
        if current_stock == 0 :
            kosong = True
        else :
            user_item_inventory[index_potion_in_inventory][1] = current_stock-1
            kosong = False
            drink_potion = True
    elif index_potion_in_inventory == -999 and not cancel  :
        print(f"anda tidak memiliki potion {type_potion}")
        kosong = True
    # Potion akan digunakan player jika beberapa kondisi berikut terpenuhi(tidak dicancel,potion blm digunakan, dan )
    if not cancel and drink_potion:    
        potion_used.append(type_potion)
        if type_potion == "strength"  and not kosong: # Efek tiap potion berlaku selama battle
            new_atk = int(user_monster[2] *1.05 )         
            user_monster[2] = new_atk
            print(f"Setelah meminum ruan ini atk power meningkat menjadi {new_atk}")
        elif type_potion == "resilience" and not kosong :
            new_def = int(user_monster[3]*1.05 )
            user_monster[3] = new_def
            print(f"Setelah meminum ramuan ini, def power meningkat menjadi {new_def}")
        elif type_potion ==  "healing" and not kosong :
            user_monster[4] = int(user_monster[4]*1.25)   
            if user_monster[4]> hp_max :
                user_monster[4]= hp_max                 
                user_monster[4] = hp_max                  
            print(f"Nyawa monster telah disembuhkan menjadi {user_monster[4]}")


def battles(database,user_id,user_role) :

    if user_role != "agent" :
        return print("Ini area bertarung agen!")
    # Mengambil data database
    user = database["user"]
    item_inventory = database["item_inventory"]
    monster_inventory = database["monster_inventory"]
    monster = database["monster"]
    # Random monster level untuk battle 
    enemy_level = randomNumberGenerator(1,5)
    user_monster_inventory = get_user_inventory(monster_inventory,user_id) # penyimpanan monster user
    user_item_inventory = get_user_inventory(item_inventory,user_id)  # penyimpanan item user
    user_monsters = level_calculation(merge_tables_by_id(monster,user_monster_inventory))  # Data user monster yang telah dikalkulasi berdasarkan level
    enemy_monsters_tables = level_calculation([random_monster_data(monster,enemy_level)])  # Data enemey monster yang telah dikalkulais berdasarkan level
    enemy_monster = enemy_monsters_tables[0]  
    print_stat_awal(monster=enemy_monster,graphics=graphics,text= f"ROARRR {enemy_monster[1]} telah muncul") # Spek awal stat monster musuh
    isFighting, user_monster = select_available_monster(user_monsters) # Memilih monster mengecek apakah bisa melanjutkan pertarungan
    hp_max = int(user_monster[4])
    turns = 1
    potion_used = []
    print_stat_awal(monster=user_monster,graphics=graphics,text=f"HUFTTT Agen telah mengeluarkan monster {user_monster[1]}") # Spek awal stat monster user
    battle_status = [turns,isFighting,False,0,0,0]   # Status battle 
    # Battle status,=> index 3 {total damage dealth user) index 4{total damage_taken_user} index 5 {penambahan oc user}
    while isFighting :
        # Meminta input perintah 
        perintah = input_perintah(turns,user_monster)
        daftar_perintah = ["1","2","3","4"]
        while perintah not in daftar_perintah :
            print("Fitur perintah tersebut belum ada")
            perintah = str(input("Pilih perintah : "))
        # jika user memilih potion maka user akan diberikan fitur meminum potion terlebib dahulu sebelum menyerang
        if perintah == "2" :
            print_potion(user_inventory=user_item_inventory)
            drink_potion(user_item_inventory=user_item_inventory,potion_used=potion_used,user_monster=user_monster,hp_max=hp_max)
        # jika user memilih menggunakan monsterball maka, monsterball akan digunakan , 
        # pada program ini kesempatan menggunakan monsterball hanya sekali tiap battle
        elif perintah == "3" :
            index_monsterball = get_index_by_id(user_id,user_item_inventory)
            get_monster = False
            if index_monsterball != -999  :
                print("Anda tidak mempunyai monsterball")
            else :
                get_monster = MonsterBall(enemy_monster)
            if get_monster :
                user_item_inventory[index_monsterball][2] -= 1  # satu buah monsterball telah digunakan 
                update_inventory_by_id(item_inventory,user_item_inventory,user_id) # updata database item_inventory
                isFighting = False # pertarunga berakhir karena monster musuh tertangkap 
                index_in_inventory = get_index_by_id(enemy_monster[0],user_monster_inventory)  
                if index_in_inventory != -999 : # mmonster yang tertangkap sudah ada di inventory
                    # converting monster to oc
                    convert_to_oc = randomNumberGenerator(0,100)
                    print(f"Sayangnya monster sudah terdapat pada inventory, sehingga monster diconvert menjadi {convert_to_oc}")
                    battle_status[5] += convert_to_oc
                else : # monster belum ada di inventory
                    new_monster = [user_id] + [enemy_monster[0]] + [enemy_monster[5]]
                    monster_inventory.append(new_monster) # menambahkan monster ke database inventory
        # Jika user memilih untuk kabur dari pertandingan
        elif perintah == "4"  :
            isFighting = False
            print("Selamat berjumpa lagi di battle selanjutnya")
        # Jika pertarungan masih dapat berlangsung, maka monster user dan monster bot akan bertarung
        if isFighting :
            oc_reward = randomNumberGenerator(0,50)
            duel(battle_status,user_monster,enemy_monster,oc_reward) # pertarungan
            turns,isFighting = battle_status[0],battle_status[1] # update elemen dengan battle status
            win = battle_status[2]
            if win and not isFighting:
                print(f"Keren monster {enemy_monster[1]} berhasil anda bunuh ") # User menang
            elif not win and not isFighting :
                print("Anda kalah, mungkin next time ,asahlah skill hoki di arena dulu dek") # user kalah

                
    # update database
    print(f"Total OC yang berhasil anda dapatkan : {battle_status[5]}")
    index_user  = get_index_by_id(user_id,user) 
    user[index_user][4] +=battle_status[5] # menambahkan oc ke database 
