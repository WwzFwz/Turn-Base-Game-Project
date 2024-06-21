from src.F08  import random_monster_data,drink_potion,print_potion,duel,select_available_monster,print_stat_awal
from src.F08 import graphics
from src.F11 import get_user_inventory,update_inventory_by_id
from src.F12 import merge_tables_by_id
from src.F07 import level_calculation 
from src.validation import get_index_by_id
def input_perintah(turns,user_monster) :
     # Fungsi mencetak perintah yang tersedia serta meminta user melakukan pemilihan perintah
    print(f"=============== Turns {turns} ({user_monster[1]})===============")
    print("1. Attack")
    print("2. Use Potion")
    print("3. Quit")
    perintah =  str(input("Pilih perintah : "))
    return perintah

def arena(database,user_id,user_role) :

    if user_role != "agent" : #check akses role
        return print("Ini area bertarung agen!")
    # database
    user = database["user"]
    item_inventory = database["item_inventory"]
    monster_inventory = database["monster_inventory"]
    monster = database["monster"]

    stage = 1 # stage awal
    user_monster_inventory = get_user_inventory(monster_inventory,user_id) # penyimpanan monster user
    user_item_inventory = get_user_inventory(item_inventory,user_id)  # penyimpanan item user
    user_monsters = level_calculation(merge_tables_by_id(monster,user_monster_inventory)) # Data user monster yang telah dikalkulasi berdasarkan level
    enemy_monsters_tables = level_calculation([random_monster_data(monster,stage)])  # Data enemey monster yang telah dikalkulais berdasarkan level
    enemy_monster = enemy_monsters_tables[0]  # enemy monster

    print(f"===========STAGES {stage}==============") 
    print_stat_awal(monster=enemy_monster,graphics=graphics,text=f"ROARRR {enemy_monster[1]} telah muncul") # base atribut monster musuh
    Arena, user_monster = select_available_monster(user_monsters) # cek apakah user memiliki monster sehingga pertarungan dapat berlangsung
    if Arena :  # pertarungan bisa aberlangsung
        print_stat_awal(monster=user_monster,graphics=graphics,text=f"HUFTTT Agen telah mengeluarkan monster {user_monster[1]}") 
        base_atk,base_def,hp_max = user_monster[2],user_monster[3],user_monster[4]
        potion_used = [] # Hp maks monster user
        turns = 1
        win_battle = False # 
        oc_rewards = [30,50,100,120,150]
        battle_status = [turns,Arena,win_battle,0,0,0] # indeks, i = 3 = damage dealth, i = 4 = damage taken, i = 5 = oc reward
    else :
        battle_status = [0,False,False,0,0,0]
    while Arena :  # Arena 
        perintah = input_perintah(turns,user_monster) # input perintah 
        daftar_perintah = ["1","2","3"]
        while perintah not in daftar_perintah :
            print("Fitur perintah tersebut belum ada")
            perintah = str(input("Pilih perintah : "))
        if perintah == "2" :  # Jika player membuka potion maka player akan diberi pilihan potion sebelum attack
            print_potion(user_inventory=user_item_inventory)
            drink_potion(user_item_inventory=user_item_inventory,potion_used=potion_used,user_monster=user_monster,hp_max=hp_max)
        elif perintah == "3"  :
            Arena = False
            print("Pergi dari arena")
        if Arena : # Arena ertarungan masih berlangsung
            oc_reward = oc_rewards[stage-1] # hadiah tahap ini
            duel(battle_status=battle_status,user_monster=user_monster,enemy_monster=enemy_monster,oc_reward=oc_reward) # monster bertarung 
            turns,Arena,win_battle = battle_status[0],battle_status[1],battle_status[2] # update keadaan battle
            if win_battle and stage != 5:
                print(f"Keren euy anda mengalahkan monster {enemy_monster[1]} ")
                print(f"Anda mendapatkan {oc_reward} pada stage ini")
                stage+=1
                new_monster = level_calculation([random_monster_data(monster,stage)])  # Pengambilan monster bot untuk stage slanjutnya
                # stage selanjutnya
                Arena = True
                win_battle = False
                enemy_monster= new_monster[0] # Monster baru
                potion_used = [] # battle selanjutnya potionnya reset
                battle_status[0] = 1 # Turns awal stage selanjutnya
                battle_status[1] = Arena  # Arena masih berlangsung
                battle_status[2] = win_battle # Belum menang pertarungan selanjutnya
                user_monster[2],user_monster[3],user_monster[4] = base_atk,base_def,hp_max  # Efek potion dan hp monster user ter reset
                print(user_monster)
                print("STAGE SELANJUTNYA : ")
                print(f"===========STAGES {stage}==============")
            elif win_battle and stage == 5 : # User telah menang hingga stage terakhir 
                Arena = False
                print(f"5{enemy_monster}")
                print(f"===========STAGES {stage}==============")
                print(f"anda telah mengalahkan final boss(monster {enemy_monster[1]})")
                print(f"Anda mendapatkan {oc_reward} pada stage ini")
            elif not win_battle  and not Arena : # user telah kalah
                stage -=1
                print(f"MONSTER ANDA WAFATTT ,TETAP SEMANGAT, ANDA KEREN TELAH BERHASIL MEMBANTAI HINGGA STAGES {stage}")

                    
    print("=======STATS========")
    print(f"Total hadiah : {battle_status[5]}")
    print(f"Jumlah stage : {stage}")
    print(f"Damage diberikan : {battle_status[3]}")
    print(f"Damage diterima : {battle_status[4]}")
    # update database
    index_user = get_index_by_id(user_id,user)
    user[index_user][4] = (int(user[index_user][4]) + battle_status[5]) # update oc
    update_inventory_by_id(item_inventory,user_item_inventory,user_id) #update data quantity potion
