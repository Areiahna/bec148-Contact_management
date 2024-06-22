import re
# Welcome to the Contact Management System project! In this project, you will apply your Python programming skills to create a functional command-line-based application that simplifies the management of your contacts. The Contact Management System will empower you to add, edit, delete, and search for contacts with ease, all while reinforcing your understanding of Python dictionaries, file handling, user interaction, and error handling.
contacts = {
"3176462145":{"name":"Big Bird","number":"3176462145","email": "arei828@yahoo.com","address":"456 Sesame St"},
"3171234567":{"name":"Elmo","number":"3171234567","email":"eli02@gmail.com","address":"123 Sesame St"}
}

def main():
    while True:
        print('''
        Menu:
        1. Add a new contact
        2. Edit an existing contact
        3. Delete a contact
        4. Search for a contact
        5. Display all contacts
        6. Export contacts to a text file
        7. Import contacts from a text file
        8. Quit 
        ''')
        ans = input("Choose an option: ")

        if ans == "1" :
            number = input("What phone number would you like to add to your contact list?: ")
            add_contact(number)
        elif ans == "2" :
            number = input("Enter the number for the contact would you like to edit: ")
            edit_contact(number)
        elif ans == "3" :
            number = input("Enter the number for the contact you would like to delete: ")
            del_contact(number)
        elif ans == "4" :
            number = input("Enter the number for the contact you're searching for: ")
            search(number)
        elif ans == "5" :
            view()
        elif ans == "6" :
            export_()
        elif ans == "7" :
            import_()
        elif ans == "8" :
            print("Thanks for using the contact management systems")
            break



def add_contact (number):
    contacts.update ({
         number : {
            "name": input("Enter contact name: "),
            "number": number,
            "email": input("Enter contact email: " ),
            "address": input("Enter contact address: ")
        }
    })
    print(f"The phone number {number}, has been added under the contact : {contacts.get(number).get("name")}")

def edit_contact(number):

    for contact in contacts.keys():
        if contact == number:
            target = contacts[contact]["name"]
            ans = input(f'''
            What would you like to update for {target}?
            1 - name
            2 - number
            3 - email
            4 - address
            ''')
            if ans == "1":
                new_name = input(f"Please enter new name: ")
                contacts[contact].update({"name":new_name})
                print(f"Updated {target}'s name to {new_name}.")
                break

            elif ans == "2":
                new_number = input(f"Please enter new number: ")
                contacts[contact].update({"number":new_number})
                print(f"Updated {target}'s number to {new_number}.")
                break
                
            elif ans == "3":
                new_email = input(f"Please enter new email: ")
                contacts[contact].update({"email":new_email})
                print(f"Updated {target}'s email {new_email}.")
                break
                
            elif ans == "4":
                new_addy = input(f"Please enter new address: ")
                contacts[contact].update({"address":new_addy})
                print(f"Updated {target}'s address to {new_addy}.")
                break
        else:
            print("That name is not in your contacts")

def del_contact(number):
    for contact in contacts:
        if contact == number:
            target = contacts[contact]["name"]
            ans = input(f"Are you sure you'd like to delete the contact: {target}? y/n :")
            if ans == "y":
                print(f"You just deleted {contacts[number]}")
                contacts.pop(number) 
                break 
            else:
                break

def search(number):
    for contact in contacts.keys():
        if contact == number:
            print(contacts[number])

def view ():
    print("\nContact List")
    print("-"*50)
    for x in contacts.keys():
        print(f"{x} - {contacts[x]}")

def export_():
    with open('mini_proj.\contacts.txt', 'w') as file:
        for contact, info in contacts.items():
            file.write(f"{contact} : {info}\n")
    print("Exported all contacts to contacts.txt")

def import_ ():
    extract = {}
    with open('mini_proj/contacts.txt', 'r') as file:
        for line in file:
            contact, contacts = line.strip().split(': ')
            extract[contacts] = contact
    print(extract)

main()