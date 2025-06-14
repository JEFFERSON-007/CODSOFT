import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from JSON file"""
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_contacts(contacts):
    """Save contacts to JSON file"""
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    """Add a new contact"""
    print("\nAdd New Contact")
    print("----------------")
    name = input("Enter name: ").strip()
    
    if name in contacts:
        print(f"Contact '{name}' already exists!")
        return
    
    phone = input("Enter phone number: ").strip()
    email = input("Enter email (optional): ").strip() or None
    address = input("Enter address (optional): ").strip() or None
    
    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    save_contacts(contacts)
    print(f"\nContact '{name}' added successfully!")

def view_contacts(contacts):
    """Display all contacts"""
    print("\nContact List")
    print("------------")
    if not contacts:
        print("No contacts found.")
        return
    
    for i, (name, details) in enumerate(contacts.items(), 1):
        print(f"{i}. {name}: {details['phone']}")

def search_contact(contacts):
    """Search for a contact by name or phone"""
    print("\nSearch Contact")
    print("--------------")
    search_term = input("Enter name or phone number to search: ").strip().lower()
    
    results = {}
    for name, details in contacts.items():
        if (search_term in name.lower()) or (search_term in details['phone']):
            results[name] = details
    
    if not results:
        print("No matching contacts found.")
        return
    
    print("\nSearch Results:")
    for name, details in results.items():
        print(f"\nName: {name}")
        print(f"Phone: {details['phone']}")
        if details['email']:
            print(f"Email: {details['email']}")
        if details['address']:
            print(f"Address: {details['address']}")

def update_contact(contacts):
    """Update an existing contact"""
    print("\nUpdate Contact")
    print("--------------")
    name = input("Enter name of contact to update: ").strip()
    
    if name not in contacts:
        print(f"Contact '{name}' not found!")
        return
    
    print("\nCurrent Details:")
    details = contacts[name]
    print(f"1. Name: {name}")
    print(f"2. Phone: {details['phone']}")
    print(f"3. Email: {details['email']}")
    print(f"4. Address: {details['address']}")
    
    print("\nEnter new details (leave blank to keep current):")
    new_name = input("Enter new name: ").strip() or name
    new_phone = input("Enter new phone: ").strip() or details['phone']
    new_email = input("Enter new email: ").strip() or details['email']
    new_address = input("Enter new address: ").strip() or details['address']
    
    if new_name != name:
        contacts[new_name] = contacts.pop(name)
    
    contacts[new_name]['phone'] = new_phone
    contacts[new_name]['email'] = new_email
    contacts[new_name]['address'] = new_address
    save_contacts(contacts)
    print("\nContact updated successfully!")

def delete_contact(contacts):
    """Delete a contact"""
    print("\nDelete Contact")
    print("--------------")
    name = input("Enter name of contact to delete: ").strip()
    
    if name not in contacts:
        print(f"Contact '{name}' not found!")
        return
    
    del contacts[name]
    save_contacts(contacts)
    print(f"Contact '{name}' deleted successfully!")

def contact_book():
    """Main contact book application"""
    contacts = load_contacts()
    
    while True:
        print("\nContact Book Menu")
        print("-----------------")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("\nGoodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-6.")

if __name__ == "__main__":
    contact_book()