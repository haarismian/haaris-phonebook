import sys


class Contact:
    """Contacts should conform to the Contact class"""

    def __init__(self, first_name, last_name, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number


contact_list = []


def add_contact():
    """Function to add new contacts to the contact list"""

    print(20*'=')
    print('You\'ve selected "Add a new contact"')

    # Ask user for first name, last name, and phone number, and validate inputs
    first_name = (str(input("Enter first name: ")))
    if first_name.isalpha() is False:
        print('Names can only contain letters, please try again')
        add_contact()

    last_name = (str(input("Enter last name: ")))
    if last_name.isalpha() is False:
        print('Names can only contain letters, please try again')
        add_contact()

    phone_number = (str(input("Enter phone number: ")))
    if phone_number.isnumeric() is False:
        print('phone numbers can only contain numbers please try again')
        add_contact()

    new_contact = Contact(first_name,
                          last_name,
                          phone_number)

    print(20*'=')
    print('First Name: ' + new_contact.first_name)
    print('Last Name: ' + new_contact.last_name)
    print('Phone Number: ' + new_contact.phone_number)
    print(20*'=')
    print('please confirm the contact details above and type "Y" to confirm, \nOR press any other key to try again\n')

    confirmation = input('Confirmation: ')

    if confirmation == 'Y' or confirmation == 'y':
        print("*****Congratulations, contact added!*****")
        print("*****Returning to main menu*****\n")
        contact_list.append(new_contact)
        main()
    else:
        # Return user to start of add contact flow if they do not confirm
        add_contact()


def search_contact():
    """Function to search entire contact list based on first name, last name, or phone number"""

    search_query = input(
        "You can search by first name, last name, or phone number, please type now and press enter (not case sensitive) \n or press enter without typing to return to main menu: ")

    if search_query == '':
        print("*****Returning to main menu*****\n")
        main()

    search_results = []

    # Functionality below will check the search query against first name, last name, or phone number for a match
    for contact in contact_list:
        sanitized_search_query = search_query.lower()
        sanitized_first_name = contact.first_name.lower()
        sanitized_last_name = contact.last_name.lower()
        sanitized_phone_number = contact.phone_number.lower()

        if sanitized_search_query in sanitized_first_name or sanitized_search_query in sanitized_last_name or sanitized_search_query in sanitized_phone_number:
            # All results that match will be added to a search results array
            search_results.append(contact)
    if not search_results:
        print('No results found, please try again')
        # Return user to start of search contact flow if no matches found
        search_contact()
    else:
        print(20*'=')
        print('Search results')
        print_contacts(search_results)
        search_contact()


def delete_contact():
    """Function to list all contacts and select one for deletion"""

    # Return user to main menu if there are no contacts
    if len(contact_list) == 0:
        print('no contacts')
        print("*****Returning to main menu*****\n")
        main()

    # Display all contacts to user with an ID that will be used to delete
    for index, contact in enumerate(contact_list):
        print(20*'=')
        print("ID: " + str(index))
        print('First Name: ' + contact.first_name)
        print('Last Name: ' + contact.last_name)
        print('Phone Number: ' + contact.phone_number)
        print(20*'=')

    # Code below continuously asks user for input until they input a valid deletion ID
    while True:
        try:
            deletion_id = int(input(
                "Please select the ID number of the contact you'd wish to delete from the list: "))
            if deletion_id > len(contact_list)-1:
                raise ValueError
            break
        except ValueError:
            print("The input was not a valid option.")
            continue

    # Display selected contact to user and ask them to confirm this is the user they wish to delete
    print("Are you sure you want to delete the following contact")
    print(20*'=')
    print("First name: " + contact_list[deletion_id].first_name)
    print("Last name: " + contact_list[deletion_id].last_name)
    print("Phone number: " + contact_list[deletion_id].phone_number)
    print(20*'=')

    deletion_confirmation = input(
        "Please type 'DELETE' (all caps) if you wish to confirm deletion: ")
    if deletion_confirmation == 'DELETE':
        del contact_list[deletion_id]
        print("\n*****Congratulations, contact deleted!*****")
        print("*****Returning to main menu*****\n")
        main()
    else:
        # Return user to beginning of deletion flow if they do not confirm
        delete_contact()


def print_main_menu():
    """Function to display main menu options to the user"""

    print(20*'=')
    print("Welcome to the UoE phonebook app")
    print("Please select one of the following options below:")
    print("1. Search for a contact.")
    print("2. Add a new contact.")
    print("3. View all contacts.")
    print("4. Delete a contact.")
    print("5. Quit the phonebook app")
    print(20*'=')


def print_all_contacts_menu():
    """Function to display all contacts view menu options to the user"""

    print("Please select one of the following options below:")
    print("1. Sort by Recently Added (default)")
    print("2. Sort by First Name")
    print("3. Sort by Last Name")
    print("4. Return to main menu")


def all_contacts_menu():
    """Function to handle user interaction with all contacts view"""
    print_all_contacts_menu()

    sort_order_menu_selection = input("Menu selection: ")
    if sort_order_menu_selection == '1':
        # Sort by recently added
        print_contacts(contact_list)
    elif sort_order_menu_selection == '2':
        # Sort by first name
        print_contacts(sorted(contact_list, key=lambda x: x.first_name))
    elif sort_order_menu_selection == '3':
        # Sort by last name
        print_contacts(sorted(contact_list, key=lambda x: x.last_name))
    elif sort_order_menu_selection == '4':
        # return to main menu
        main()
    else:
        print(
            "\n!!!!! Invalid selection. Select from options [1-4] !!!!!\n")

    all_contacts_menu()


def display_all_contacts():
    """Displays all contacts"""

    # Return user to main menu if there are no contacts
    if len(contact_list) == 0:
        print('no contacts')
        print("*****Returning to main menu*****\n")
        main()

    else:
        print_contacts(contact_list)
        all_contacts_menu()


def print_contacts(contacts):
    """Function to take a list of contacts and display them with proper format"""

    for contact in contacts:
        print(20*'=')
        print('First Name: ' + contact.first_name)
        print('Last Name: ' + contact.last_name)
        print('Phone Number: ' + contact.phone_number)
        print(20*'=')


def main():
    """Main menu and start page"""

    menu_selection = ''

    print_main_menu()
    menu_selection = input("Menu selection: ")

    if menu_selection == '1':
        search_contact()
    elif menu_selection == '2':
        add_contact()
    elif menu_selection == '3':
        display_all_contacts()
    elif menu_selection == '4':
        delete_contact()
    elif menu_selection == '5':
        print("\nExiting.")
        sys.exit("Goodbye!")

    else:
        print(
            "\n!!!!! Invalid selection. Select from options [1-5] !!!!!\n")


if __name__ == '__main__':
    main()
