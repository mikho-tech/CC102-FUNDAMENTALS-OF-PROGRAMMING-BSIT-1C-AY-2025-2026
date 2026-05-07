class calendar:
    def __init__(self):
        self.years = {}

    def is_leap_year(self, year):
        if year % 4 == 0:
            return True
        else:
            return False
    def get_days_in_month(self, year, month):
        match month:
            case 1:
                return 31
            case 2:
                if self.is_leap_year(year):
                    return 29
                else:
                    return 28
            case 3:
                return 31
            case 4:
                return 30
            case 5:
                return 31
            case 6:
                return 30
            case 7:
                return 31
            case 8:
                return 31
            case 9:
                return 30
            case 10:
                return 31
            case 11:
                return 30
            case 12:
                return 31
            case _:
                return -1

    def get_month_name(self, month):
        match month:
            case 1:
                return "January"
            case 2:
                return "February"
            case 3:
                return "March"
            case 4:
                return "April"
            case 5:
                return "May"
            case 6:
                return "June"
            case 7:
                return "July"
            case 8:
                return "August"
            case 9:
                return "September"
            case 10:
                return "October"
            case 11:
                return "November"
            case 12:
                return "December"
            case _:
                return "Unknown"
            
def is_date_valid(self, day, month, year):
        if year < 2020 or year > 2030:
            print("[ERROR] Year must be between 2020 and 2030 only.")
            return True
        if month < 1 or month > 12:
            print("[ERROR] Month must be between 1 and 12 only.")
            return True
        max_day = self.get_days_in_month(year, month)
        if day < 1 or day > max_day:
            print(f"[ERROR] Day must be between 1 and {max_day} for {self.get_month_name(month)} {year}!")
            return True

list = []
dictionary = calendar ()

while True:
    print("---MAIN MENU---")
    print(" ")
    print("1. Add an Event")
    print("2. View Events on a Date")
    print("3. View All Events")
    print("4. Delete an Event")
    print("5. Exit")

    main = input("Please select an option (1-5): ")

    if main == "1":
        print("---ADD AN EVENT---")
        print("---Enter the date---")
        year = int(input("Enter the year (YYYY-YYYY): "))
        month = int(input("Enter the month (1-12): "))
        day = int(input("Enter the day (1-31): "))

        if dictionary.is_date_valid(day, month, year):
            continue

        event_name = str(input("Enter the event name: "))

        if dictionary.is_leap_year(year):
            print(f"{year} is a leap year.")

        list.append([year, month, day, event_name])
        print(f"SUCCESS | Event: {event_name} added for {dictionary.get_month_name(month)} {day}, {year}")


    elif main == "2":
        print("---VIEW EVENTS ON A DATE---")
        year = int(input("Enter the year (YYYY-YYYY): "))
        month = int(input("Enter the month (1-12): "))
        day = int(input("Enter the day (1-31): "))

        if dictionary.is_date_valid(day, month, year):
            continue

        event_name = str(input("Enter the event name: "))
        print("Year: " + str(year))
        print("Month: " + dictionary.get_month_name(month))
        print("Day: " + str(day))
        print("Event Name: " + event_name)

    elif main == "3":
        print("---VIEW ALL EVENTS---")
        print(list)

    elif main == "4":
        print("---DELETE AN EVENT---")
        event_name = input("Enter the event name to delete: ")

        for item in list:
            if item [3] == event_name:
                list.remove(item)
                print("Event deleted successfully!")
                break
        else:
            print("Event not found.")

    elif main == "5":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid option. Please select a number between 1 and 5.")