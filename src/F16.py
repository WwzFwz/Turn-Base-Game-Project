from src.F15 import save
import sys

def exit(database):
    validation = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")

    while not ((validation.upper() == "Y") or (validation.upper() == "N")):
        validation = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
        
    if validation.upper() == "Y":
        save(database)
        sys.exit()
    else:
        sys.exit()
