

users:list=[
    {'name':'Mateusz','location':'Poznań','posts':100},
    {'name':'Maciej','location':'Łódż','posts':200},
    {'name':'Maciej01','location':'Siedlice','posts':300},
    {'name':'Konrad','location':'Grudziądz','posts':400},
]


def get_user_info(users_data:list)->None:
    for user in users_data:
        print(f"Twój znajomy {user['name']} z miejscowości {user['location']} opublikował {user['posts']} postów.")

get_user_info(users)