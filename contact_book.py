import json

CONTACTS_FILE = 'contacts.json'

def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(name, phone, email):
    contacts[name] = {
        'phone': phone,
        'email': email
    }
    save_contacts(contacts)

def remove_contact(name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
    else:
        print("Contact not found.")

def search_contact(name):
    return contacts.get(name, "Contact not found.")

def main():
    global contacts
    contacts = load_contacts()

    while True:
        print("\nContact Book")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif choice == '2':
            name = input("Enter name of the contact to remove: ")
            remove_contact(name)
        elif choice == '3':
            name = input("Enter name of the contact to search: ")
            print(search_contact(name))
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
