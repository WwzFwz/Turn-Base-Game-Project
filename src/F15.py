import os
import time
from src import utilityfunction as uf

def save(temp_data):
    folder_name = input("Masukkan nama folder: ")
    path = "C:/Users/ASUS/TUBESDAS/" + folder_name
    if not(os.path.exists(path)):
        os.mkdir(path)
        print("Saving...\n")
        time.sleep(2)
        print(f"Membuat folder {folder_name}")
        time.sleep(1)
        print(f"Berhasil menyimpan data di folder {folder_name}!")
    else:
        print("Saving...\n")
        time.sleep(2)
        print(f"Berhasil menyimpan data di folder {folder_name}!")
    uf.array_to_csv(temp_data["user"], path + "/user.csv")
    uf.array_to_csv(temp_data["monster"], path + "/monster.csv")
    uf.array_to_csv(temp_data["monster_shop"], path + "/monster_shop.csv")
    uf.array_to_csv(temp_data["monster_inventory"], path + "/monster_inventory.csv")
    uf.array_to_csv(temp_data["item_inventory"], path + "/item_inventory.csv")
    uf.array_to_csv(temp_data["item_shop"], path + "/item_shop.csv")
