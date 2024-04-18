import time
from datetime import datetime

def calculate_age_in_seconds(birthdate):
    # Konvertera födelsedatumet till en tidsstämpel
    birth_timestamp = time.mktime(time.strptime(birthdate, "%Y-%m-%d"))
    
    # Beräkna aktuell tid
    current_timestamp = time.time()
    
    # Beräkna ålder i sekunder
    age_in_seconds = current_timestamp - birth_timestamp
    
    return age_in_seconds

def calculate_age_in_years(birthdate):
    birth_date = datetime.strptime(birthdate, '%Y-%m-%d')
    
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the difference between the current date and the birthdate
    age = current_date.year - birth_date.year
    
    # Check if the birthday for this year has passed or not
    if (current_date.month, current_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    
    return age

from datetime import datetime

def calculate_age_in_days(birthdate): 
    # Convert the birthdate string to a datetime object
    birth_date = datetime.strptime(birthdate, '%Y-%m-%d')
    
    # Get the current date
    current_date = datetime.now()
    
    # Calculate the difference between the current date and the birthdate
    age_in_days = (current_date - birth_date).days
    
    return age_in_days

if __name__ == "__main__":
    birthdate = input("Ange ditt födelsedatum (ÅÅÅÅ-MM-DD): ")
    age_in_days = calculate_age_in_days(birthdate)
    print("Du är ungefär", age_in_days, "dagar gammal.")
