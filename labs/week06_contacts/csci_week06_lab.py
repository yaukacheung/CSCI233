"""
Contact Book App

Objectives:
- Use dictionaries to store structured contact data.
- Perform CRUD operations:
    Create, Read, Update, Delete
- Use unique contact names as dictionary keys.
- Use a set to store unique cities.
"""


# --------------------------------------------------
# Contact Data
# --------------------------------------------------

contacts = {}

# A set automatically keeps cities unique.
cities = set()


# --------------------------------------------------
# Create - Add Contact
# --------------------------------------------------

def add_contact():
    """Add a new contact to the contact book."""

    name = input("Enter contact name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    # Dictionary keys must be unique.
    if name in contacts:
        print("A contact with that name already exists.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email address: ").strip()
    city = input("Enter city: ").strip()

    # Store contact information in a nested dictionary.
    contacts[name] = {
        "phone": phone,
        "email": email,
        "city": city
    }

    # Add city to the set.
    if city:
        cities.add(city)

    print(f"Contact '{name}' added successfully.")


# --------------------------------------------------
# Read - Search Contact
# --------------------------------------------------

def search_contact():
    """Search for a contact by name."""

    name = input("Enter contact name to search: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    contact = contacts[name]

    print("\n--- Contact Information ---")
    print(f"Name:  {name}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print(f"City:  {contact['city']}")


# --------------------------------------------------
# Read - List All Contacts
# --------------------------------------------------

def list_contacts():
    """Display all contacts."""

    if not contacts:
        print("No contacts found.")
        return

    print("\n========== All Contacts ==========")

    for name, contact in contacts.items():
        print(f"\nName:  {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"City:  {contact['city']}")

    print("\n==================================")


# --------------------------------------------------
# Update - Edit Contact
# --------------------------------------------------

def update_contact():
    """Update an existing contact."""

    name = input("Enter contact name to update: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    contact = contacts[name]

    print("\nPress Enter to keep the existing value.")

    new_phone = input(f"Phone [{contact['phone']}]: ").strip()
    new_email = input(f"Email [{contact['email']}]: ").strip()
    new_city = input(f"City [{contact['city']}]: ").strip()

    if new_phone:
        contact["phone"] = new_phone

    if new_email:
        contact["email"] = new_email

    if new_city:
        contact["city"] = new_city
        cities.add(new_city)

    print(f"Contact '{name}' updated successfully.")


# --------------------------------------------------
# Delete - Remove Contact
# --------------------------------------------------

def delete_contact():
    """Delete a contact from the contact book."""

    name = input("Enter contact name to delete: ").strip()

    if name not in contacts:
        print("Contact not found.")
        return

    del contacts[name]

    print(f"Contact '{name}' deleted successfully.")

    # Rebuild the city set so it contains only cities
    # currently used by contacts.
    update_cities()


# --------------------------------------------------
# Update City Set
# --------------------------------------------------

def update_cities():
    """Update the set of unique cities from current contacts."""

    cities.clear()

    for contact in contacts.values():
        if contact["city"]:
            cities.add(contact["city"])


def list_cities():
    """Display all unique cities."""

    if not cities:
        print("No cities found.")
        return

    print("\n========== Unique Cities ==========")

    for city in sorted(cities):
        print(city)

    print("===================================")


# --------------------------------------------------
# Menu
# --------------------------------------------------

def display_menu():
    """Display the main menu."""

    print("\n========== CONTACT BOOK ==========")
    print("1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. List all contacts")
    print("6. List unique cities")
    print("7. Exit")
    print("==================================")


# --------------------------------------------------
# Main Program
# --------------------------------------------------

def main():
    """Run the Contact Book application."""

    while True:
        display_menu()

        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            add_contact()

        elif choice == "2":
            search_contact()

        elif choice == "3":
            update_contact()

        elif choice == "4":
            delete_contact()

        elif choice == "5":
            list_contacts()

        elif choice == "6":
            list_cities()

        elif choice == "7":
            print("Thank you for using Contact Book!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


# Start the application
if __name__ == "__main__":
    main()
