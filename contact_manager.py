import csv
import os

FILENAME = "contacts.csv"

# Ensure that contacts.csv file exists with headers
def init_file():
    if not os.path.exists(FILENAME):
        with open(FILENAME, mode= "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Phone', 'Email'])

# Add a contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email : ")

    with open(FILENAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, phone, email])

    print("✅ contact added successfully!")

# view all contacts
def view_contacts():
    with open(FILENAME, "r", newline="") as file:
        reader = csv.reader(file)
        next(reader) # Skip header
        print("\n📒 Contact List:")
        for row in reader:
            print(f"Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")

# Search a contact by name
def search_contact():
    search_name = input("Enter a name to search:").lower()
    found = False

    with open(FILENAME, "r", newline= "") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if search_name in row[0].lower():
                print(f"🔍Found: Name: {row[0]}, Phone: {row[1]}, Email: {row[2]}")
                found = True

    if not found:
        print("❌ No contact found.")     

# Delete a contact by name
def delete_contact():
    name_to_delete = input("Enter name to delete: ").lower()
    contacts = []

    with open(FILENAME, mode='r') as file:
        reader = csv.reader(file)
        contacts = list(reader)

    header = contacts[0]
    contacts = [row for row in contacts[1:] if name_to_delete not in row[0].lower()]
    
    with open(FILENAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(contacts)

    print("🗑️ Contact deleted if it existed.")    

# Main loop
def main():
    init_file()
    while True:
        print("\n📱 Contact Manager Menu")
        print("1. Add contact")
        print("2. View all contacts")
        print("3. Search contact")
        print("4. Delete contact")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❗Invalid choice. Please try again.")

# Run the App
main()


     
