# Art Club Management System

members = []
events = []
artworks = []
financials = []
#Nafisha's Part
def add_member():
    name = input("Enter member's name: ")
    age = input("Enter age: ")
    art_form = input("Enter art form: ")
    members.append([name, age, art_form])
    print(f"{name} added successfully!")
#Mim's Part
def view_members():
    if len(members) == 0:
        print("No members in the club.")
    else:
        print("\nArt Club Members:")
        print("------------------------------------------------")
        print("No. | Name          | Age | Art Form")
        print("------------------------------------------------")
        for i in range(len(members)):
            # Print the member's number, name, age, and art form in a formatted way
            print(f"{i+1}.  | {members[i][0]:12} | {members[i][1]:3} | {members[i][2]}")
        # Print the ending line for the table
        print("------------------------------------------------")

#Farhana's Part
def remove_member():
    name = input("Enter the name of the member to remove: ")
    for i in range(len(members)):
        if members[i][0] == name:
            members.pop(i)
            print(f"Member '{name}' removed successfully!")
            return
    print("Member not found!")
#Mounota's Part
def add_event():
    name = input("Enter event name: ")
    date = input("Enter event date (YYYY-MM-DD):")
    description = input("Enter event description: ")
    events.append([name, date, description])
    print("Event {0} added successfully!".format(name))


def view_events():
    if len(events) == 0:
        print("No upcoming events.")
    else:
        print("\nUpcoming Events:")
        print("------------------------------------------------")
        print("No. | Event Name    | Date       | Description")
        print("------------------------------------------------")
        for i in range(len(events)):
            print(f"{i+1}.  | {events[i][0]:12} | {events[i][1]} | {events[i][2]}")
        print("------------------------------------------------")

def remove_event():
    name = input("Enter the name of the event to remove: ")
    for i in range(len(events)):
        if events[i][0] == name:
            events.pop(i)
            print(f"Event '{name}' removed successfully!")
            return
    print("Event not found!")
#Nafi's Part
def add_artwork():
    artwork_name = input("Enter artwork name: ")
    artwork_type = input("Enter artwork type: ")
    member_name = input("Enter the member's name who created the artwork: ")
    artworks.append([artwork_name, artwork_type, member_name])
    print(f"Artwork '{artwork_name}' added successfully!")

def view_artworks():
    if len(artworks) == 0:
        print("No artworks available.")
    else:
        print("\nArt Club Artworks:")
        print("------------------------------------------------")
        print("No. | Artwork Name  | Type       | Created by")
        print("------------------------------------------------")
        for i in range(len(artworks)):
            print(f"{i+1}.  | {artworks[i][0]:12} | {artworks[i][1]:10} | {artworks[i][2]}")
        print("------------------------------------------------")
#Farhana's Part
def manage_finance():
    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Balance")
    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        amount = float(input("Enter income amount (in Tk): "))
        financials.append(["Income", amount])
        print(f"Income of {amount:.2f} Tk added successfully!")
    elif choice == '2':
        amount = float(input("Enter expense amount (in Tk): "))
        financials.append(["Expense", amount])
        print(f"Expense of {amount:.2f} Tk added successfully!")
    elif choice == '3':
        total_income = sum([entry[1] for entry in financials if entry[0] == "Income"])
        total_expense = sum([entry[1] for entry in financials if entry[0] == "Expense"])
        balance = total_income - total_expense
        print(f"Current balance: {balance:.2f} Tk")
    else:
        print("Invalid choice!")
#Torikul's Part
def main():
    while True:
        print("\n==== Art Club Management System ====")
        print("1. Add Member")
        print("2. View Members")
        print("3. Remove Member")
        print("4. Add Event")
        print("5. View Events")
        print("6. Remove Event")
        print("7. Add Artwork")
        print("8. View Artworks")
        print("9. Manage Finance")
        print("10. Exit")

        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            add_member()
        elif choice == '2':
            view_members()
        elif choice == '3':
            remove_member()
        elif choice == '4':
            add_event()
        elif choice == '5':
            view_events()
        elif choice == '6':
            remove_event()
        elif choice == '7':
            add_artwork()
        elif choice == '8':
            view_artworks()
        elif choice == '9':
            manage_finance()
        elif choice == '10':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 10.")

main()