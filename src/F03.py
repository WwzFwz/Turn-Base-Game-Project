def logout(logged_in_user):
    if logged_in_user != None:
        print("logout telah berhasil")
    else:
        print(f'Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout.')
    return None,None,None
