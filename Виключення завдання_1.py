# принимать на вход номер месяца, вернуть его название

month_func = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}
month = int(input("Select month number- "))
if month > 0:
    if month < 13:
        for key, value in month_func.items():
            if month == value:
                    print(key)
    else:
        print("Select number from 1 to 12")