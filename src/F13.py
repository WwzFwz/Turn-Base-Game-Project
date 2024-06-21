
from src.validation import * 
from src.F12 import table_interface

def is_monster_exist(monster:str,table_monster:list[list])-> bool :  
    # Fungsi mengecek apakah monster merupakan baagian dari database monster
    found = False 
    i = 1
    while not found and (i<len(table_monster)) :
        if monster.lower() == table_monster[i][1].lower() :
            found = True
        i +=1
    return found    
def input_monster_not_exist(monster:str,table_monster)->str :
    # Fungsi meminta user unntuk memberi masukan monster yang belum ada di database monster
    while is_monster_exist(monster,table_monster) :
        monster = str(input("Masukkan monster yang belum ada : "))
    return monster
 

def monster_management(database,user_role:str) :


    if user_role.lower() == "admin" : # cek akses
        isManaging = True
        tabel_monster = database['monster']

        while isManaging :
            print("SELAMAT DATANG DI DATABASE PARA MONSTER !!!\n1. Tampilkan semua Monster \n2. Tambah Monster baru\n3.Cancel")
            aksi = str(input("Pilih aksi(1/2/3) :")) 
            if aksi == "1" :
                table_interface(tabel_monster,"DATAABASE MONSTER KOSONG")
            elif aksi == "2" : 
                nama_monster = str(input("Masukkan type/nama monster :"))
                # Meminta user untuk memberikan masukan nama monster dengan type string dan belum ada di database
                while not is_all_same_type(nama_monster,check_integer=False) or is_monster_exist(nama_monster,tabel_monster) :
                    nama_monster = input_untill_type_valid(nama_monster,message="Masukkan type/nama monster : ",type="string")
                    nama_monster = input_monster_not_exist(nama_monster,tabel_monster)
                         
                attack_power =  str(input("Masukkan attack power : "))
                # Meminta user untuk memberikan masukan attack power  dengan type int 
                while not is_all_same_type(attack_power,check_integer=True)  :
                    attack_power = input_untill_type_valid(attack_power,message="Masukkan attack power : ",type="integer")

                def_power = str(input("Masukkan def power (range 0 - 50) : "))
                # Meminta user untuk memberikan masukan adef power  dengan type int dan dengan range 0-50
                while not is_all_same_type(def_power,check_integer=True) or  not is_range_valid(def_power,51) :
                    def_power = input_untill_type_valid(def_power,message="Masukkan def_power (range 0 - 50) : ",type="integer")
                    def_power = input_untill_range_valid(def_power,51,"Masukkan range def yang benar (0-50) : ")  

                hp_monster = str(input("Masukkan HP monster : "))
                # Meminta user untuk memberikan masukan hp   dengan type int
                while not is_all_same_type(hp_monster,check_integer=True) :
                    hp_monster = input_untill_type_valid(hp_monster,message="Masukkan HP monster : ",type="integer")
                
                id_monster = str(len(tabel_monster)) # id monster baru terurut
                new_monster = [int(id_monster),nama_monster,int(attack_power),int(def_power),int(hp_monster)]

                # cetak monster yang berhasil dibuat
                print("\n \n Monster baru telah berhasil dibuat")  
                print(f"Type : {nama_monster} ")
                print(f"ATK Power : {attack_power}")
                print(f"DEF Power : {def_power}")
                print(f"HP : {hp_monster}\n")

                tambahkan = str(input("Tambahkan monster ke database(Y/N) : ")).lower()     
                if tambahkan == "y" :
                    isManaging = False
                    tabel_monster.append(new_monster)
                    print("Monster berhasil ditambahkan")
                    next_command = str(input("Ingin menambahkan monster lain?(Y/N) : ")).lower()
                    if next_command == "y" :
                        isManaging = True
                else : # tidak jadi ditambahkan
                    print("Monster gagal ditambahkan")
            elif aksi =="3" :
                isManaging = False
            else :
                print("Input tidak valid")
    else : 

        print("Anda tidak memiliki akses pada monster management" )
