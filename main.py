from utils.model import users
from utils.controler import get_user_info, add_user, remove_user, update_user, get_map


def main():
    print('========= MENU =========')
    print('0 - zakończ program')
    print('1 - wyświetl co u znajomych')
    print('2 - dodaj znajomego')
    print('3 - usuń znajomego')
    print('4 - zaktualizuj dane znajomego')
    print('5 - przygotuj mapę znajomych')
    print('========================')

    while True:
        choice: str = input('Wybierz opcję menu: ')

        if choice == '0':
            break
        elif choice == '1':
            get_user_info(users)
        elif choice == '2':
            add_user(users)
        elif choice == '3':
            remove_user(users)
        elif choice == '4':
            update_user(users)
        elif choice == '5':
            get_map(users)
        else:
            print('Niepoprawna opcja, spróbuj ponownie.')


if __name__ == '__main__':
    main()