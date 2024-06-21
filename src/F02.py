import src.utilityfunction as uf


def login(database:dict,logged_in_user,user_id,user_role):
    registered_users = database["user"]
    if logged_in_user == None:
        username = input("Username: ")
        password = input("Password: ")
        registered_username = uf.get_data_by_column_title(registered_users, 'username')
        if username not in registered_username:
            print("Username tidak terdaftar!")
            user_id,user_role = None,None
        else: 
            user_password = uf.get_row(registered_users, 'username', username)[0][2]
            if password == user_password:
                logged_in_user = username
                user_id = int(uf.get_row(registered_users, 'username', username)[0][0])
                user_role = uf.get_row(registered_users, 'username', username)[0][3]
                if user_role == "Admin":
                    print(f'Selamat datang, Admin {username}!\nMasukkan command "HELP" untuk daftar command yang dapat kamu panggil.')
                else:
                    print(f'Selamat datang, Agent {username}!\nMasukkan command "HELP" untuk daftar command yang dapat kamu panggil.')
            else:   
                print("Password salah!")
                user_id,user_role = None,None
    else:
        print(f'Login gagal!\nAnda telah login dengan username {logged_in_user} silahkan lakukan "LOGOUT" sebelum melakukan login kembali.')
    return logged_in_user, user_id, user_role
