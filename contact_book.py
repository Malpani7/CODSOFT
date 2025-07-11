import json
import os
from winreg import QueryInfoKey

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    else:
        return[]

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)


def add_contacts():
    name = input("Enter Name:")
    phone = input("Enter Phone Number:")
    email = input("Enter Email:")
    address = input("Enter Address:")
     
    contacts = load_contacts()
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }) 
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!\n")


def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("NO contacts found.\n")
        return
    print("\n-----Contact List-----")
    for idx, contact in enumerate(contacts, start=1):
        print(f"{idx}. Name     : {contact['name']}")
        print(f"   Phone    : {contact['phone']}")
        print(f"   Email    : {contact['email']}")
        print(f"   Address  : {contact['address']}\n")


def search_contacts():
    query = input("Enter name or phone number to search:") 
    contacts = load_contacts()
    found = False 
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            print("\nContact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}\n")
            found = True
    if not found:
        print("Contact not found.\n")


def update_contacts():
    query = input("Enter name of the contact to update:")
    contacts = load_contacts()
    for contact in contacts:
        if query.lower() == contact['name'].lower():
            print("Leave blank if you don't want to change a field.")
            new_name = input(f"Enter new name ({contact['name']}): ") or contact['name']
            new_phone = input(f"Enter new phone ({contact['phone']}): ") or contact['phone']
            new_email = input(f"Enter new email ({contact['email']}): ") or contact['email']
            new_address = input(f"Enter new address ({contact['address']}): ") or contact['address']

            contact['name'] = new_name
            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address

            save_contacts(contacts)
            print(f"Contact '{new_name}' updated successfully!\n")
            return
    print("Contact not found.\n")


def delect_contacts():
    query = input("Enter name of the contact to delect:")
    contacts = load_contacts()
    for contact in contacts:
        if query.lower() == contact['name'].lower():
            contacts.remove(contact)
            save_contacts(contacts)
            print(f"Contact '{contact['name']}' deleted successfully!\n")
            return
    print("Contact not found.\n")


def main_menu():
    while True:
        print("---- Contact ----")
        print("1.Add Contact")
        print("2. View Contact List")
        print("3.Search Contact")
        print("4.Update Contact")
        print("5.Delect Contact")
        print("6.Exit")
        choice = input("Enter your choice (1-6):")

        if choice == '1':
            add_contacts()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            update_contacts()
        elif choice == '5':
            delect_contacts()
        elif choice == '6':
            print("Exit")
            break
        else:
            print("Invaild choice, please try again.\n")

print("Testing if file runs...")

if __name__ == "__main__":
    print("Running main_menu() now...")
    main_menu()
