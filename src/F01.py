from src.utilityfunction import get_data_by_column_title
import src.validation as val
import src.F00 as RNG

def register(logged_in_user: str,database:dict):
    registered_users = database["user"]
    monster_inventory = database["monster_inventory"]
    monster = database["monster"]
    if logged_in_user == None:
        logged_in_user = input("Masukkan username: ")
        password = input("Masukkan password: ")

        if val.check_username_availability(registered_users,logged_in_user) and val.check_username_validity(logged_in_user):
            generated_id = RNG.randomNumberGenerator(1, 1000)

            while val.is_registered_id(registered_users,generated_id):
                generated_id = RNG.randomNumberGenerator(1, 1000)
            registered_users.append([str(generated_id), logged_in_user, password, "Agent", "0"])
            
            print("\nSilahkan pilih salah satu monster sebagai monster awalmu.")
            monster_name = get_data_by_column_title(monster, "type")
            monster_id = get_data_by_column_title(monster, "id")

            for i in range(1, len(monster)):
                print(f"{i}. {monster[i][1]}")
            monster_choice = int(input("\nMonster pilihanmu: "))
            monster_inventory.append([generated_id, monster_id[monster_choice-1], monster_name[monster_choice-1]])
            print(f"Selamat datang Agent {logged_in_user}. Maria kita mengalahkan Dr. Asep Spakbor dengan {monster_name[monster_choice-1]}!")

        else:
            if not val.check_username_availability(registered_users,logged_in_user)  :
                print(f"\nUsername {logged_in_user} sudah terpakai, silahkan gunakan username lain!")
            else:
                print("\nUsername hanya boleh berisi alfabet, angka, underscore, dan strip!")
    
    else:
        print(f'\nRegister gagal!\nAnda telah login dengan username {logged_in_user} silahkan lakukan "LOGOUT" sebelum melakukan register.')
    return database

