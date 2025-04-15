from utils.model import users
from utils.controller import get_user_info, add_user


def main():
    print('===========MENU=============')
    print('0 - zakoncz program')
    print('1 - wyswietl co u znajomych')
    print('2 - dodaj znajomego')
    print('============================')
    while True:
        choice:str=input('wybierz opcje MENU: ')
        if choice == '0':break
        if choice == '1':get_user_info(users)
        if choice == '2':add_user(users)



if __name__ == '__main__':
    main()
