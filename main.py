from utils.model import users
from utils.controler import get_user_info, add_user, remove_user, update_user


def main():
    print('=========menu=========')
    print('0 - zakończ program')
    print('1 - wyświetl co u znajomych')
    print('2 - dodaj znajomego')
    print('3 - usuń znajomego')
    print('4 - zauktaizuj dane znajomego')
    print('======================')
    while True:
        choice: str = input('wybierz opcię menu: ')
        if choice == '0': break
        if choice == '1': get_user_info(users)
        if choice == '2': add_user(users)
        if choice == '3': remove_user(users)
        if choice == '4': update_user(users)


if __name__ == '__main__':
    main()
