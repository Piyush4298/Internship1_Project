import sqlite3
from Contacts import Contact_db_code as cdc

db = sqlite3.connect(':memory:')
cdc.create_table(db)
print('Welcome to Contacts Manager')
print('--------------')
choice = ''


def show_menu():
    print('MENU')
    print('--------------')
    print('1. Add Contact')
    print('2. Delete a Contact')
    print('3. Edit Contact')
    print('4. View All Contacts')
    print('5. Search Contact(by name or number)')
    print('6. Exit')
    print('-------------------')
    choice = input('Enter your choice: ')
    return choice


while choice != '6':
    choice = show_menu()
    if choice == '1':
        name = input('Enter name: ')
        number = int(input('Enter number: '))
        if (name,) in cdc.current_db_info(db, 1,name):
            print('Already in the contacts')
        elif (number,) in cdc.current_db_info(db, 2,number):
            print('Number already in the list')
        else:
            cdc.add_user(db, name, number)
            print('Contact saved successfully!!!!!')

    elif choice == '2':
        con_to_be_deleted = input('Which contact to be deleted(enter its exact name): ')
        if (con_to_be_deleted,) not in cdc.current_db_info(db, 1,con_to_be_deleted):
            print('No such contact exists in your Contacts')
        else:
            cdc.delete_user_by(db, con_to_be_deleted)
            print('Deleted contact successfully!!!!!!')

    elif choice == '3':
        edit_choice = input('What do u want to update(0 for name and 1 for number): ')
        con_to_be_edited = input('Enter contact to be edited:(enter exact name ) ')
        if edit_choice == '1' and (con_to_be_edited,) in cdc.current_db_info(db, 1,con_to_be_edited):
            new_num = input('Enter new number')
            cdc.update_user_number(db, con_to_be_edited, new_num)
            print('Contact edited successfully!!!!')
        elif edit_choice == '0' and (con_to_be_edited,) in cdc.current_db_info(db, 1,con_to_be_edited):
            new_name = input('Enter new name')
            cdc.update_user_name(db, con_to_be_edited, new_name)
            print('Contact edited successfully!!!!')
        else:
            print('Number or Name entered must not be matching ,Try again')
            continue

    elif choice == '4':
        print('Your contact list :')
        con_lst = cdc.current_db_info(db)
        for i, j in sorted(con_lst):
            print('Name: ', i, '| Number: ', j)

    elif choice == '5':
        con_to_be_searched = input('Enter Name or Number to be searched: ')
        for name, number in cdc.current_db_info(db):
            if con_to_be_searched == name or con_to_be_searched == str(number):
                print('Name: ', name, '| Number: ', number)
                break
        else:
            print('No results found!!')
    elif choice == '6':
        break
    else:
        print('Invalid choice please choose from the MENU and try again!!!!!!!!')


