import clock

year = 2024
sec_in_day = 86400
days_in_year = 365


#def age_in_seconds(age_in_years):
#    return age_in_years * days_in_year * sec_in_day

def game():
    name = input("Your name: \n")
    birth_year = (input("Which year were born (give it in 4 digits like 2001): \n"))
    birth_month = (input("Which month were born (2 digits like 01): \n"))
    birth_day = (input("Which day were born (2 digits like 25): \n"))
    birth_date = birth_year + "-" + birth_month + "-" + birth_day
    
    age_in_years = clock.calculate_age_in_years(birth_date)

    print("Chose an alternetive:")
    print("1. Days you have lived\n")
    print("2. Year you were born\n")
    print("3. Seconds you have lived\n")

    val = input("Choose ONE alternitive: \n")

    if val == "1":
        greet_and_give_question(name, age_in_years)
    elif val == "2":
        val2(name, age_in_years)
    elif val == "3":
        val3(name, age_in_years)
    else:
        print("Not an alternitive")

def greet_and_give_question(name, age):
    print("You choose alternitive 1\n")
    print(f"Hello {name} how are you doing? You are turning/have turned {clock} days old this year!\n")
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

def val2(name, age):
    print("You choose alternitive 2\n")
    print(f"Hello {name}, how are you doing? You are turning/have turned {age} years old this year, that means you are born in {year - age}!\n")
    val_c(age)

def val3(name, age):
    print("You choose alternitive 3\n")
    print(f"Hello {name} how are you doing? You are turning/have turned {clock.age_in_seconds(date)} seconds old this year!\n")
    val_c(age)
    

def val_c(age):
    val2 = input("Do you want to continue? Yes or No: ").lower()
    if val2 == "no":
        print("You have ended the game.")
    if val2 == "yes":
        print("Password")
        password = int(input("Type password (It is how many seconds YOU have lived): "))
        if password ==  age_in_seconds(age): 
            print("GAME COMPLETED!\n")
        else: print("Game Over\n")



if __name__ == "__main__":
    game()