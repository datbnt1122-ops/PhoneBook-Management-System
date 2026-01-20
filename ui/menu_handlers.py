def main_menu():
    while True:
        print_header("Phone Book Management System")
        options = [
            "View all contacts",
            "Search contacts",
            "Add contact",
            "Update contact",
            "Delete contact"
        ]
        print_menu(options)

        choice = get_choice(len(options))

        if choice == 1:
            view_contacts()
        elif choice == 2:
            search_contacts()
        elif choice == 3:
            add_contact()
        elif choice == 4:
            update_contact()
        elif choice == 5:
            delete_contact()
        elif choice == 0:
            show_message("Goodbye!")
            break


def view_contacts():
    print_header("Contact List")
    display_contacts(contacts)
    pause()


def search_contacts():
    print_header("Search Contacts")
    keyword = input_non_empty("Enter keyword: ").lower()

    results = [
        c for c in contacts
        if keyword in c["name"].lower()
        or keyword in c["phone"]
        or keyword in c["email"].lower()
    ]

    display_contacts(results)
    pause()


def add_contact():
    print_header("Add New Contact")

    contact = {
        "name": input_non_empty("Name: "),
        "phone": input_phone("Phone (10 digits): "),
        "email": input("Email: "),
        "group": input("Group: "),
        "notes": input("Notes: ")
    }

    contacts.append(contact)
    show_message("Contact added successfully.")
    pause()


def update_contact():
    print_header("Update Contact")
    display_contacts(contacts)

    if not contacts:
        pause()
        return

    index = get_choice(len(contacts)) - 1
    if index < 0:
        return

    contact = contacts[index]

    contact["name"] = input(f"Name ({contact['name']}): ") or contact["name"]
    contact["phone"] = input(f"Phone ({contact['phone']}): ") or contact["phone"]
    contact["email"] = input(f"Email ({contact['email']}): ") or contact["email"]
    contact["group"] = input(f"Group ({contact['group']}): ") or contact["group"]
    contact["notes"] = input(f"Notes ({contact['notes']}): ") or contact["notes"]

    show_message("Contact updated successfully.")
    pause()


def delete_contact():
    print_header("Delete Contact")
    display_contacts(contacts)

    if not contacts:
        pause()
        return

    index = get_choice(len(contacts)) - 1
    if index < 0:
        return

    confirm = input("Are you sure you want to delete this contact? (y/n): ").lower()
    if confirm == "y":
        contacts.pop(index)
        show_message("Contact deleted successfully.")
    else:
        show_message("Deletion cancelled.")

    pause()
\
