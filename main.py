from src.F01 import register
from src.F02 import login
from src.F03 import logout
from src.F04 import menu_and_help
from src.F05 import owcadex
from src.F07 import inventory
from src.F08 import battles
from src.F09 import arena
from src.F10 import shop
from src.F11 import laboratory
from src.F12 import shop_management 
from src.F13 import monster_management
from src.F14 import load
from src.F15 import save
from src.F16 import exit
from src.jackpot import Jackpot


logged_in_user, user_id, user_role = None, None, None


database = load()

while True : 
    command = str(input(">>>>> "))
    if command.lower() == "login" :
        logged_in_user,user_id,user_role = login(database,logged_in_user,user_id,user_role)
    elif command.lower() == "help" :
        menu_and_help(user_role,logged_in_user)
    elif command.lower() == "register" :
        database= register(logged_in_user,database)
    elif command.lower() == "logout" : 
        logged_in_user,user_id,user_role = logout(logged_in_user)
    elif command.lower() == "battle" :
        battles(database,user_id,user_role)
    elif command.lower() == "inventory" : 
        inventory(database,user_id,user_role)
    elif command.lower() == "arena" :
        arena(database,user_id,user_role)
    elif command.lower() == "laboratory" :
        laboratory(database,user_id,user_role)
    elif command.lower() == "jackpot" :
        Jackpot(user_id,user_role,database)
    elif command.lower() == "owcadex" :
        owcadex(user_role, database["monster"])
    elif command.lower() =="shop management" :
        database["monster_shop"],database["item_shop"]  =shop_management(database,user_role)
    elif command.lower() == "shop" :
        shop(database,user_id,user_role)
    elif command.lower() == "monster management" :
        monster_management(database,user_role)
    elif command.lower() == "save" :
        save(database)
    elif command.lower() == "exit" :
        exit(database)
    else :
        print('Command tidak terdaftar! Silahkan masukkan command "HELP" untuk melihat command yang dapat kamu panggil.')
