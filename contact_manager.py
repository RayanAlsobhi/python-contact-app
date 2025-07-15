import os 

# create file to store contacts

CONTACTS_FILE='contacts.txt'

# function to add the contacts
def add_contact():
    name = input('Enter name: ')
    phone = input('Enter phone number: ')
    email = input('Enter email: ')

    with open(CONTACTS_FILE,'a') as f:
        f.write(f'{name},{phone},{email}\n')

    print('Contact added successfully.')  


# function to view all contatcts

def view_contacts():
    if not os.path.exists(CONTACTS_FILE):
        print('No contacts found.')  
        return
    
    with open(CONTACTS_FILE,'r') as f:
        contacts = f.readlines()

        if not contacts:
            print('No contatcts found.')
            return
        
        print('\n Contact List: ')

        for i , contacts in enumerate(contacts , start=1):
            name,phone,email = contacts.strip().split(',')
            print(f'{i}. Name: {name}, Phone: {phone}, Email: {email}')


# function to search a contact by name 

def search_contact():
    if not os.path.exists(CONTACTS_FILE):
        print('No contacts or file found.')  
        return
    search_name = input('Enter name to search: ').lower()
    found = False

    with open(CONTACTS_FILE,'r') as f:
        for line in f:
            name , email , phone = line.strip().split(',')
            if search_name in name.lower():

                print(f'Found: Name: {name}, Phone: {phone}, Email: {email} ')
                found = True

    if not found:  
        print('No matching contact found.')        


# control panel to start the program

def show_menu():
    while True:

        print('\n Contact Manager')  
        print('1. Add Contact')
        print('2. View Contacts')   
        print('3. Search Contacts')      
        print('4. Exit')

        choice = input('Select Options (1 - 4): ')

        if choice == '1':
            add_contact()

        elif choice == '2':
            view_contacts()

        elif choice == '3':
            search_contact()

        elif choice == '4':
            print('Exit.. ')
            break        

        else:
            print('Ivalid choice. Try again.')




if __name__ == '__main__':
    show_menu()



                

