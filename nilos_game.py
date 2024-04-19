import datetime_helper
import print_cool_graphics

print("HAHHAHHAAA THIS IS MY NEW CHANGE TO YOUR CODE")
year = 2024
sec_in_day = 86400
days_in_year = 365


#def age_in_seconds(age_in_years):
#    return age_in_years * days_in_year * sec_in_day

def game():
    print_cool_graphics.print_title()
    name = input("Your name: \n").lower()
    if name == "nilo":
        print("Oh it's you master, welcome!")
    else:
        print("Hmm, not the master huh...")
    birth_year = (input("Which year were you born (YYYY): \n"))

    while not birth_year.isdigit():
        print("Please enter a valid year in digits.")
        # You might want to handle this error, like asking for input again or exiting the program
        birth_year = (input("Which year were born (YYYY): \n"))

    
    birth_month = (input("Which month were you born (MM): \n"))
    birth_day = (input("Which day were you born (DD): \n"))
    birth_date = birth_year + "-" + birth_month + "-" + birth_day
    
    age_in_years = datetime_helper.calculate_age_in_years(birth_date)

    print("Chose an alternetive:")
    print("1. Days you have lived\n")
    #instead of "2", i can have how many days until birhtday.
    print("2. Days until birthday\n")
    print("3. Seconds you have lived\n")

    val = input("Choose ONE alternitive: \n")

    if val == "1":
        greet_and_give_question(name, age_in_years, birth_date)
    elif val == "2":
        val2(name, birth_date)
    elif val == "3":
        val3(name, age_in_years, birth_date)
    else:
        print("Not an alternitive")

def greet_and_give_question(name, age, birth_date):
    print("You choose alternitive 1\n")
    print(f"Hello {name} how are you doing? You have turned {datetime_helper.calculate_age_in_days(birth_date)} days old today!\n")
    print("You are lucky you choose number 1. Now you will get to answer a question!\n")
    answer_a_question(age)

def answer_a_question(age):
    print("Wich year did Gustav Vasa become king?")
    print("a. 1623\n")
    print("b. He was never king, he was a fisherman.\n")
    print("c. 1523\n")
    new_choice = input("Answer here:\n")
    if new_choice == "c":
        print("CORRECT!\n")
        val_c(age)
    elif new_choice == "b":
        print("No, wrong answer😂🤙\n")
    elif new_choice == "a":
         print("No, wrong answer😂🤙\n")

def val2(name, birth_date):
    print("You choose alternitive 2\n")
    days_until_birthday = datetime_helper.days_until_birthday(birth_date)
    print(f"You have {days_until_birthday} until your next birthday")
    val_c()

def val3(name, age, date):
    print("You choose alternitive 3\n")
    print(f"Hello {name} how are you doing? You are turning/have turned {datetime_helper.calculate_age_in_seconds(date)} seconds old this year!\n")
    val_c()
    

def val_c():
    val2 = input("Do you want to continue? Yes or No: ").lower()
    if val2 == "no":
        print("You have ended the game.")
    elif val2 == "yes":
        print("Password")
        password = (input("Type password: ")).lower()
        if password == "password": 
            print("GAME COMPLETED!\n")
        else:
            print("Game Over\n")

# Nu kan du använda val3 och val_c-funktionerna som du önskar



if __name__ == "__main__":
    game()
