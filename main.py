from tkinter import *
from typing import Tuple, List
import csv

# Getting the information from the file
with open("IdentityBot Tartu Discord User Verification List - Sheet1.csv", "r") as file:
    file_dict = csv.DictReader(file)

    # Creating the dictionary of users
    user_dict = {}
    for line in file_dict:
        key = (line['Floor #'], line['Suite #'], line['Room #'])
        if key not in user_dict and key == ("0", "0", "0"):
            user_dict[key] = [[line['First Name'].lower(), line["Last Name"].lower()]]
        elif key not in user_dict:
            user_dict[key] = [line['First Name'].lower(), line["Last Name"].lower()]
        else:
            user_dict[key].append([line['First Name'], line["Last Name"]])

    # Creating the graphic interface
    root = Tk()
    root.title("Tartu College Identifier")
    root.resizable(False, False)
    widgets = []

    # Functions for buttons

    def create_greeting_admin() -> None:
        """
        Creates the window greeting an admin
        """
        admin_label = Label(root, text="We have verified that you are an admin!\n\nClick on the 'Exit' button to "
                                       + "close the program")
        admin_exit_button = Button(root, text="Exit", command=root.destroy)
        admin_label.grid(row=0, column=0, padx=10, pady=10)
        admin_exit_button.grid(row=1, column=0, pady=10)


    def create_greeting_resident() -> None:
        """
        Creates a window greeting a resident
        """
        resident_label = Label(root, text="We have verified that you are a resident!\n\nClick on the 'Exit' button to "
                                          + "close the program")
        resident_exit_button = Button(root, text="Exit", command=root.destroy)
        resident_label.grid(row=0, column=0, padx=10, pady=10)
        resident_exit_button.grid(row=1, column=0, pady=10)


    def verify_name(name: List[str], key: Tuple[str, str, str]) -> None:
        """
        Compares the list name, containing the first name and the last name strings inputted by the user, to the data
        our file to verify if the key belongs to them
        """
        # Clearing the previous window
        for widget in widgets:
            widget.destroy()
        # Comparing the name and verifying whether the user is an admin
        if name in user_dict[key] and key == ("0", "0", "0"):
            create_greeting_admin()
        elif user_dict[key] == name:
            create_greeting_resident()
        else:
            # Creating Error Window
            name_error_label = Label(root, text="Your name was does not correspond to this key.\n\nIf you are a "
                                                + "resident please contact our\nteam to troubleshoot. Meanwhile, "
                                                + "please \nmake sure you entered your name correctly.\n\nPlease press "
                                                + "'Exit' to close the program")
            name_exit_button = Button(root, text="Exit", command=root.destroy)
            name_error_label.grid(row=0, column=0, padx=10, pady=10)
            name_exit_button.grid(row=1, column=0, pady=10)


    def create_name_window(key: Tuple[str, str, str]) -> None:
        """
        Creates the Window for the Verification of the Name. Takes the user key for further verification.
        """
        # Creating Widgets
        name_label = Label(root, text="We found your key in our database!\n\nTo finish verifying, please enter the " +
                                      "following\ninformation and then click 'Next'")
        widgets.append(name_label)
        firstname_label = Label(root, text="What is your first name?")
        widgets.append(firstname_label)
        firstname_entry = Entry(root, width=35)
        widgets.append(firstname_entry)
        lastname_label = Label(root, text="What is your last name?")
        widgets.append(lastname_label)
        lastname_entry = Entry(root, width=35)
        widgets.append(lastname_entry)
        next_button_name = Button(root, text="Next", command=lambda: verify_name([firstname_entry.get().lower(),
                                                                                  lastname_entry.get().lower()], key))
        widgets.append(next_button_name)
        # Placing widgets in the grid
        name_label.grid(row=0, column=0, pady=10, padx=10)
        firstname_label.grid(row=1, column=0, pady=(10, 0), padx=(10, 100))
        firstname_entry.grid(row=2, column=0, pady=(0, 10))
        firstname_entry.insert(0, "Ex: John (delete this)")
        lastname_label.grid(row=3, column=0, padx=(10, 100))
        lastname_entry.grid(row=4, column=0, pady=(0, 10))
        lastname_entry.insert(0, "Ex: Snow (delete this)")
        next_button_name.grid(row=5, column=0, pady=10)


    def verify_key(key: Tuple[str, str, str]) -> None:
        """
        Compares the tuple key, containing the floor, suite, and room integers inputted by the user, to the data in our
        file to verify whether it is a key
        """
        # Clearing the previous window
        for widget in widgets:
            widget.destroy()
        # Comparing the key
        if key in user_dict:
            create_name_window(key)
        else:
            # Creating Error Window
            key_error_label = Label(root, text="Your key was not found in our database.\n\nIf you are a resident, " +
                                               "please contact our\nteam to troubleshoot. Meanwhile, please\nmake " +
                                               "sure you entered the numbers correctly.\n\nPlease press 'Exit' to " +
                                               "close the program")
            key_exit_button = Button(root, text="Exit", command=root.destroy)
            key_error_label.grid(row=0, column=0, padx=10, pady=10)
            key_exit_button.grid(row=1, column=0, pady=10)


    def create_key_window() -> None:
        """
        Creates the window for the verification of the key
        """
        # Clearing the previous window
        for widget in widgets:
            widget.destroy()
        # Creating widgets
        key_label = Label(root, text="Please enter the following information and then click 'Next'")
        widgets.append(key_label)
        floor_label = Label(root, text="What is your floor number?")
        widgets.append(floor_label)
        floor_entry = Entry(root, width=30)
        widgets.append(floor_entry)
        suite_label = Label(root, text="What is your suite number?")
        widgets.append(suite_label)
        suite_entry = Entry(root, width=30)
        widgets.append(suite_entry)
        room_label = Label(root, text="What is your room number?")
        widgets.append(room_label)
        room_entry = Entry(root, width=30)

        widgets.append(room_entry)
        next_button_key = Button(root, text="Next", command=lambda: verify_key((floor_entry.get(), suite_entry.get(),
                                                                                room_entry.get())))
        widgets.append(next_button_key)
        # Placing widgets in the grid
        key_label.grid(row=0, column=0, pady=(10, 20))
        floor_label.grid(row=1, column=0, padx=(10, 50))
        floor_entry.grid(row=2, column=0, padx=(10, 10), pady=(0, 20))
        floor_entry.insert(0, "Ex: 1 (delete this)")
        suite_label.grid(row=4, column=0, padx=(10, 50))
        suite_entry.grid(row=5, column=0, padx=(10, 10), pady=(0, 20))
        suite_entry.insert(0, "Ex: 1 (delete this)")
        room_label.grid(row=7, column=0, padx=(11, 50))
        room_entry.grid(row=8, column=0, padx=(10, 10), pady=(0, 10))
        room_entry.insert(0, "Ex: 1 (delete this)")
        next_button_key.grid(row=9, column=0, pady=(0, 20))


    # Creating the welcome page
    welcome_label = Label(root, text="Welcome to the Tartu College Identifier!\nWe will be asking for information to " +
                                     "verify that you are a resident\n\nClick 'Next' to continue")
    widgets.append(welcome_label)
    next_button = Button(root, text="Next", pady=0, command=create_key_window)
    widgets.append(next_button)

    welcome_label.grid(row=0, column=0, pady=10)
    next_button.grid(row=1, column=0, pady=20)

    root.mainloop()
