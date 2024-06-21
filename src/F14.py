import sys
import argparse
import os
import time
from src.utilityfunction  import read_csv
from src.validation import check_path_validity

def integer_adjustment (tables,column_exception) :
    for i in range(1,len(tables)) :
        for j in range(len(tables[0])) :
            if j not in column_exception :
                tables[i][j] = int(tables[i][j])
    return tables



def converting(folder_name:str)-> dict :

    path = "C:/Users/ASUS/TUBESDAS/" + folder_name

    if check_path_validity(path): 
        print("LOADING...")
        time.sleep(2)
        # Baca csv ubah ke tables , type blm di adjust (masih string)
        user = read_csv(path + "/user.csv")
        monster = read_csv(path + "/monster.csv")
        monster_shop = read_csv(path + "/monster_shop.csv")
        monster_inventory = read_csv(path+"/monster_inventory.csv")
        item_shop = read_csv(path + "/item_shop.csv")
        item_inventory =read_csv(path + "/item_inventory.csv")


        database = {    
            "user" : integer_adjustment(user,[1,2,3]),
            "monster" : integer_adjustment(monster,[1]),
            "monster_shop" : integer_adjustment(monster_shop,[]),
            "monster_inventory" : integer_adjustment(monster_inventory,[]),
            "item_shop" : integer_adjustment(item_shop,[0]),
            "item_inventory" :integer_adjustment(item_inventory,[1])
        }
    elif folder_name == "":
        print("Tidak ada nama folder diberikan!")
        #program berhenti
    else:
        print(f"Folder {folder_name} tidak ditemukan!")
        #program berhenti
    return database
    

def load () :
    parser = argparse.ArgumentParser()
    parser.add_argument("name", type=str,help="name of saved game", nargs="?", const='')
    args = parser.parse_args()
    folder = args.name

    if folder == None:
        print('Tidak ada nama folder yang diberikan!\nUsage : python main.py <nama folder>\nJika kamu belum pernah bermain, silahkan masukkan "python main.py database".')
        sys.exit()
    else:
        path = "C:/Users/ASUS/TUBESDAS/" + folder
        if (os.path.exists(path)):
            database = converting(folder)
        else:
            print(f"Folder {folder} tidak ditemukan!")
            sys.exit()
    print('Selamat datang di Program OWCA!\nMasukkan command "HELP" untuk melihat daftar command yang dapat kamu panggil.')
    return database
