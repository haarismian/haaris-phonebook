# UoE Contact Book Application

Word count: 437

# What Is This?

This is a simple Python application intended to implement a contact book.

# Available functionality

1. Add as many contacts as user prefers (with confirmation feature)
2. Search for individual contacts based on first name, last name, or phone number
3. View all saved contacts and sort by recently added, first name, or last name
4. Delete contacts (with confirmation feature)
5. Keyboard interaction functionality

# How To run this application

## Terminal

1. Ensure you have python installed (run command 'python' or 'python3' in terminal to verify) or you can install from: https://www.python.org/downloads/
2. Using terminal navigate to the directory where the `phonebook.py` file is saved
3. run command `python3 phonebook.py`
4. Enjoy experience in terminalfollowing on-screen instructions to navigate app

## Python IDLE

1. Open IDLE
2. Open the `phonebook.py` file
3. Select Run from the command bar
4. Enjoy experience in
   IDLE following on-screen instructions to navigate app

# Algorithm Implementation

## Insertion

1. The user will be asked for a first name, last name, and phone number, all of which will be validated
2. If the strings pass validation they will be turned into a Contact object and added to the contact_list array and the user will be congratulated
3. If they do not pass validation the user will be asked to enter the information again

<img width="468" alt="image" src="https://user-images.githubusercontent.com/13083798/204175210-28858bf0-f6be-4712-9fcf-41c324d074a8.png">

<img width="480" alt="image" src="https://user-images.githubusercontent.com/13083798/204179951-96a7afc8-5a02-453a-b1ac-d80fb02cb1dc.png">

## Deletion

1. The user will be shown their list of contacts along with an ID #
2. The user will select one of the ID #s to delete
3. Once a contact is selected, the contact will be displayed and the user will have to confirm they want to delete by typing "DELETE"
4. Incorrect ID #s or not using the correct confirmation phrase will return the user to the beginning of the flow

<img width="468" alt="image" src="https://user-images.githubusercontent.com/13083798/204175412-ccbbf01b-a0e6-48ad-9eb1-d76119d7b91e.png">

<img width="580" alt="image" src="https://user-images.githubusercontent.com/13083798/204180037-a42316e4-577b-4593-8ec1-503bc0baea6c.png">

## Sorting

1. When the user chooses to view all their contacts, they will receive options to change the sort order by recently added, first name, or last name
2. Selecting the option will re-render the list of contacts with the appropriate sorting

<img width="468" alt="image" src="https://user-images.githubusercontent.com/13083798/204175422-e7dec43e-edf1-4561-b860-4beef5020d4f.png">

<img width="412" alt="image" src="https://user-images.githubusercontent.com/13083798/204180651-5c5af742-2ed6-4cbb-b777-a101a6a66f5f.png">

## Searching

1. The user can select to search for a particular contact from the main menu
2. The user can search by first name, last name, or phone number, the search string the user types in will be checked against the entire contact list if any of the contact properties CONTAINS the search string (exact match not necessary)

<img width="468" alt="image" src="https://user-images.githubusercontent.com/13083798/204175429-ed2a3fee-edf8-42a4-9c13-0b1c69d3f0db.png">

<img width="802" alt="image" src="https://user-images.githubusercontent.com/13083798/204180722-eeb22571-325e-46aa-bf2f-740f80b41ce3.png">
