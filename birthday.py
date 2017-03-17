import csv

OUTFILE = "birthday.csv"
INFILE = "birthday.csv"

def enterBirthday():
    birthday = input('Enter the Birthday in dd/mm/yy format')
    name = input('Enter the Name of the person')
    outfile_write = open(OUTFILE,"a+")
    writer = csv.writer(outfile_write)
    writer.writerow((name,birthday))

    outfile_write.close()

def checkBirthday():
    infile_read = open(INFILE,"r")
    rows = csv.reader(infile_read)
    date = input('Enter date ')
    #age = calAge(date)
    for row in rows:
        if row[1] == date:
            print(row[0] + "'s birthday is on " + date + "\n\n")#Print it saying "x's birthday is on <date>, and their age is y"
    infile_read.close()

def checktodayBirthday():
    #Take the date from system, and see who's birthday is today
    return 1
def calcAge(date):
    #Calculate the age of the person, based on the birthday and current date
    return 1


if __name__ == '__main__':

    while True:
        print("Choose one of the following options")
        print("1. Entering new birthday")
        print("2. Checking who's birthday is it today")
        print("3. Exit the application")
        choice = int(input('Enter Choice: '))

        if choice == 1:
            enterBirthday()
        elif choice == 2:
            checkBirthday()
        elif choice == 3:
            break
        else:
            print("Wrong option, enter again")

    print("\nThank you for using the application")





