def take_monster_id_level (user_id, monster_inventory):
    monster_id = []
    monster_level = []
    for i in range (len(monster_inventory)-1):
        if (user_id == int(monster_inventory[1+i][0])):
            monster_id.append(monster_inventory[1+i][1])
            monster_level.append(monster_inventory[1+i][2])
    return (monster_id, monster_level)

def base_monster_in_inventory (monster_id,user_id,monster_array,monster_inventory):
    monster_level = take_monster_id_level(user_id,monster_inventory)[1]
    base_monster = []
    for i in range (len(monster_id)):
        for j in range (len(monster_array)-1):
            if (int(monster_id[i]) == int(monster_array[1+j][0])):
                base_monster.append(monster_array[1+j]+list(monster_level[i]))
    print(base_monster)
    return (base_monster)
  
def level_calculation(base_monster):
    monster_in_inventory = base_monster
    for i in range (len(base_monster)):  
        header = False   
        if str(monster_in_inventory[i][0]).lower() == "id" :
            header = True
        if (str(monster_in_inventory[i][5]  )!= "1")and  not header :
            #atk_power
            monster_in_inventory[i][2] = (float(monster_in_inventory[i][2]) + (float(monster_in_inventory[i][2])) * (float(monster_in_inventory[i][5])*0.1))
            #def_power
            monster_in_inventory[i][3] = (float(monster_in_inventory[i][3]) +(float(monster_in_inventory[i][3])) * (float(monster_in_inventory[i][5])*0.1))
             #health
            monster_in_inventory[i][4] = (float(monster_in_inventory[i][4]) +(float(monster_in_inventory[i][4])) * (float(monster_in_inventory[i][5])*0.1))
        elif (str(monster_in_inventory[i][5])) == "1" and not header :
            monster_in_inventory[i][2] = float(monster_in_inventory[i][2])
            monster_in_inventory[i][3] = float(monster_in_inventory[i][3])
            monster_in_inventory[i][4] = float(monster_in_inventory[i][4])
    return(monster_in_inventory)


def take_item_id (user_id,item_inventory):
    item_id = []
    for i in range (len(item_inventory)-1):
        if (user_id == int(item_inventory[1+i][0])):
            item_id.append(item_inventory[1+i])
    return (item_id)

def display_inventory(user_id,current_inventory_item,current_inventory_monster,owca_coin):
    count = 0
    print("============ INVENTORY LIST (User ID :",str(user_id)+") ============")
    print("Jumlah O.W.C.A. Coin-mu sekarang",owca_coin)
    for i in range(len(current_inventory_monster)):
        print(str(i+1)+". Monster       (Name:",current_inventory_monster[0+i][1],", Lvl:",current_inventory_monster[0+i][5],", HP:",str(current_inventory_monster[0+i][4])+")")
        count+=1
    for j in range(len(current_inventory_item)):
        if (current_inventory_item[0+j][1] == "Monster Ball"):
            print(str(count+1+j)+". Monster Ball  (Qty:",current_inventory_item[0+j][2]+")")
        else:
            print(str(count+1+j)+". Potion        (Type:",current_inventory_item[0+j][1],", Qty:",str(current_inventory_item[0+j][2])+")")

def inventory(database,user_id):
    monster_inventory = database["monster_inventory"]
    item_inventory = database["item_inventory"]
    monster_array = database["monster"]
    owca_coin = 837
    monster_id = take_monster_id_level(user_id,monster_inventory)[0]
    base_monster = base_monster_in_inventory(monster_id,user_id,monster_array,monster_inventory)
    current_inventory_monster = level_calculation(base_monster)
    current_inventory_item = take_item_id(user_id,item_inventory)
    display_inventory(user_id,current_inventory_item,current_inventory_monster,owca_coin)
    count_monster = int(len(current_inventory_monster))
    count_item = int(len(current_inventory_item))
    inventory_command = input()
    while (inventory_command != "KELUAR"):
        if (1 <= int(inventory_command) <= (count_monster + count_item)):
            if(1 <= int(inventory_command) <= count_monster):
                take_monster = current_inventory_monster[int(inventory_command)-1]
                print("Monster")
                print("Name           :",take_monster[1])
                print("ATK Power      :",take_monster[2])
                print("DEF Power      :",take_monster[3])
                print("HP             :",take_monster[4])
                print("Level          :",take_monster[5])
            if(count_monster < int(inventory_command) <= (count_monster + count_item)):
                take_item = current_inventory_item[int(inventory_command)-1-count_monster]
                if(take_item[1]=="Monster Ball"):
                    print("Monster Ball")
                    print("Quantity :",take_item[2])
                else:
                    print("Potion")
                    print("Type      :",take_item[1])
                    print("Quantity  :",take_item[2])
                print("Ketikkan id untuk menampilkan id item :")
                inventory_command = input()
        else:
            print("Command diluar range, silahkan masukan range valid")
            print("Ketikkan id untuk menampilkan id item :")
            inventory_command = input()
    
