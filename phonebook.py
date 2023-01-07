class Phonebook:
    # in initialization, we're creating dictionary to store data (name, surname etc.)
    def __init__(self):
        self.jotter = {}
        # making version of program private
        self.__version = 1

    # creating setter to control version of our program
    def set_version(self, version):
        if version == 1:
            self.__version = version
        else:
            print("invalid program version")

    # creating getter to get info about version of a program
    def get_version(self):
        return self.__version

    # here we're adding person with following parameters (name as key, value (surname, phone, mobile phone))
    def add_person(self, key, val):
        self.jotter[key] = val
        return 'successfully added'

    # here we're looking for name that we're deleting (if we found one)
    def del_name(self, name):
        if name in self.jotter:
            del self.jotter[name]
            return f'{name} deleted'
        return "can't find this name in address book!"

    # all information
    def info(self):
        return self.jotter.items()

    def print_all_info(self):
        print('Showing all users in address book >:')
        # here we're showing all users which was added to our dictionary (key,value)
        for name, data in book.info():
            data = ' '.join(data)
            print(name, data)

    def print_mobile(self):
        print('Printing mobile with username >:')
        # here we're showing all users which was added to our dictionary , but first showing mobile numbers of them
        for name, data in book.info():
            data = ''.join(data[2])
            print(data, name)

    def print_name(self):
        print('Printing users name first >:')
        # here we're showing all users which was added to our dictionary , but first showing name of them
        for name, data in book.info():
            data = ' '.join(data)
            print(name, data)

    def print_surname(self):
        print('Printing users surname first >:')
        # here we're showing all users which was added to our dictionary , but first showing surname of them
        for name, data, in book.info():
            data = ' '.join(data[:3])
            print(data, name)

    def sort_by_name(self):
        print('Sorting address book by name')
        # creating list to store split and inserted name
        data1 = []
        # creating list to store sorted users
        new_data = []
        for name, data in book.info():
            # creating a variable to store data (surname, number of phone, number of mobile)
            data = ' '.join(data)
            # splitting all data
            data1 = data.split()
            # inserting name of each user
            data1.insert(0, name)
            # appending all information to new list
            new_data.append(data1)
        # sorting info(in our case it's names)
        # creating lambda to sort in each list every name, index of name is - 0
        new_data.sort(key=lambda x: x[0])
        for i in new_data:
            print(i)

    def sort_by_number(self):
        print('Sorting address book by number')
        # creating list to store split and inserted name
        data1 = []
        # creating list to store sorted users
        new_data = []
        for name, data in book.info():
            # creating a variable to store data (surname, number of phone, number of mobile)
            data = ' '.join(data)
            # splitting all data
            data1 = data.split()
            # inserting name of each user
            data1.insert(0, name)
            # appending all information to new list
            new_data.append(data1)
        # sorting phone numbers in reverse (the largest number - first)
        # creating lambda to sort in each list every number, index of numbers is - 2
        new_data.sort(key=lambda x: x[2], reverse=True)
        for i in new_data:
            print(i)

    def sort_by_surname(self):
        print('Sorting address book by surname')
        # creating list to store split and inserted name
        data1 = []
        # creating list to store sorted users
        new_data = []
        for name, data in book.info():
            # creating a variable to store data (surname, number of phone, number of mobile)
            data = ' '.join(data)
            # splitting all data
            data1 = data.split()
            # inserting name of each user
            data1.insert(0, name)
            # appending all information to new list
            new_data.append(data1)
        # sorting surnames
        # creating lambda to sort in each list every surname, index of surname is - 1
        new_data.sort(key=lambda x: x[1])
        for i in new_data:
            print(i)

    def sort_by_mobile(self):
        print('Sorting address book by mobile phone')
        # creating list to store split and inserted name
        data1 = []
        # creating list to store sorted users
        new_data = []
        for name, data in book.info():
            # creating a variable to store data (surname, number of phone, number of mobile)
            data = ' '.join(data)
            # splitting all data
            data1 = data.split()
            # inserting name of each user
            data1.insert(0, name)
            # appending all information to new list
            new_data.append(data1)
        # sorting mobile phones in reverse (the largest number - first)
        # creating lambda to sort in each list every mobile number, index of mobile number is - 3
        new_data.sort(key=lambda x: x[3], reverse=True)
        for i in new_data:
            print(i)

    def save_info(self):
        print('Copying all users in address book... >:')
        # here we're creating txt file and writing all information from our dictionary (jotter)
        with open("info.txt", "w") as file:
            for name, data in book.info():
                data = ' '.join(data)
                return file.write(name + ' ' + data + '\n')


# creating an instance of a class
book = Phonebook()
book.set_version(version=1.0)

print("-" * 35)
print(f'Phonebook version {book.get_version()}')
print("-" * 35)
print('''  1 - Add contact
  2 - Delete contact
  3 - Change contact
  4 - Show all contacts
  5 - Print mobile first
  6 - Print usernames first
  7 - Print surnames first
  8 - Sort address book by name 
  9 - Sort address book by surname
 10 - Sort address book by number
 11 - Sort address book by mobile number
 12 - Copying all info into txt file
 13 - To exit from program''')
print("-" * 35)
# endless cycle
while True:
    # selecting in menu
    command = input("Enter command >: ")
    if command == '1':
        # entering name
        name = input("Enter name (min length - 3 symbols, use only words): ")
        # creating endless cycle to check 'if, else' construction
        while True:
            # if our name have 3 or more symbols and have ONLY words returns TRUE
            if len(name) >= 3 and name.isalpha():
                print('name added')
                break
            else:
                print('invalid name, try again!')
                name = input('Enter name: ')
        # entering surname
        surname = input("Enter surname (min length - 2 symbols, use only words): ")
        # creating endless cycle to check 'if, else' construction
        while True:
            # if our name have 2 or more symbols and have ONLY words returns TRUE
            if len(surname) >= 2 and surname.isalpha():
                print('surname added')
                break
            else:
                print('invalid surname, try again!')
                surname = input('Enter surname again: ')
        # entering phone number
        phone_num = input("Enter phone number, starts with 56 or 49 (symbols - 6, example - 563020 ): ")
        # creating endless cycle to check 'if, else' construction
        while True:
            # if our number starts with 56 or 49 , have length of six or more symbols (only numbers) returns True
            if phone_num.startswith('56') and len(phone_num) == 6 and phone_num.isdigit() or phone_num.startswith(
                    '49') and len(phone_num) == 6 and phone_num.isdigit():
                print('right! home number added')
                break
            else:
                print('this is not home number, try again! (starts with 56 or 49 and have length of six symbols)')
                phone_num = input("Enter phone number: ")
        # entering mobile phone
        mobile_num = input('Enter mobile phone, starts with 8, need 11 symbols (example 87013603540): ')
        # creating endless cycle to check 'if, else' construction
        while True:
            # if our number starts with 8, have length of eleven symbols (only numbers) returns True
            if mobile_num.startswith('8') and len(mobile_num) == 11 and mobile_num.isdigit():
                print('Right! mobile number added')
                break
            else:
                print('this is not mobile number, try again! (starts with 8 and have length of 11 symbols)')
                mobile_num = input('Enter mobile number: ')
        # adding to dictionary all data (name as key, surname, phone_num, mobile_num as values)
        print(book.add_person(name, [surname, phone_num, mobile_num]))

    # entering name to delete
    elif command == '2':
        name = input("Enter name to delete >:  ")
        print(book.del_name(name))

    # changing information (need to enter name)
    elif command == '3':
        # entering name of user in phonebook (already created user)
        name = input('Enter name to change (re-wright) >: ')
        # if we have name in dictionary returns True
        if name in book.jotter:
            while True:
                print('name found in address book!')
                print('press 1 to change surname')
                print('press 2 to change phone number')
                print('press 3 to change mobile number')
                print('press 4 to exit')
                choose = input('press number - ')

                if choose == '1':
                    surname = input('enter surname - ')
                    # if our name have 2 or more symbols and have ONLY words returns TRUE
                    if len(surname) >= 2 and surname.isalpha():
                        print('surname changed')
                        print(book.add_person(name, [surname, phone_num, mobile_num]))
                        break
                    else:
                        print('invalid surname, try again!')

                elif choose == '2':
                    phone_num = input("Enter phone number, starts with 56 or 49 (symbols - 6, example - 563020 ): ")
                    # if our number starts with 56 or 49 , have length of six(only numbers) returns True
                    if phone_num.startswith('56') and len(
                            phone_num) == 6 and phone_num.isdigit() or phone_num.startswith('49') \
                            and len(phone_num) == 6 and phone_num.isdigit():
                        print('Right! home number changed')
                        print(book.add_person(name, [surname, phone_num, mobile_num]))
                        break
                    else:
                        print(
                            'this is not home number, try again! (starts with 56 or 49 and have length of 6 '
                            'symbols)')

                elif choose == '3':
                    mobile_num = input('Enter mobile phone, starts with 8, need 11 symbols (example 87013603540): ')
                    # if our number starts with 8, have length of eight or more symbols (only numbers) returns True
                    if mobile_num.startswith('8') and len(mobile_num) == 11 and mobile_num.isdigit():
                        print('Right! mobile number changed')
                        print(book.add_person(name, [surname, phone_num, mobile_num]))
                        break
                    else:
                        print(
                            'this is not mobile number, try again (starts with 8 and have length of 11 symbols)')

                # exiting from cycle
                elif choose == '4':
                    break
                else:
                    print('unknown command')
        # if we entered user which is not from address book
        else:
            print('Name not found in address book')

    elif command == '4':
        book.print_all_info()

    elif command == '5':
        book.print_mobile()

    elif command == '6':
        book.print_name()

    elif command == '7':
        book.print_surname()

    elif command == '8':
        book.sort_by_name()

    elif command == '9':
        book.sort_by_surname()

    elif command == '10':
        book.sort_by_number()

    elif command == '11':
        book.sort_by_mobile()

    elif command == '12':
        book.save_info()

    elif command == '13':
        print('exiting....')
        break

    else:
        print('unknown command')
