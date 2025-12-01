import datetime
import time

movie_name = str(input("Enter the movie name: "))
movie_release_year = int(input("Enter the movie release year (YYYY): "))

current_year = datetime.datetime.now().year
years_released = current_year - movie_release_year

if len(movie_name) < 3:
    while True:
        print("Please Enter a valid movie name (4 characters)")
        time.sleep(0.5)
        movie_name = str(input("Enter the movie name: "))
        if len(movie_name) >= 3:
            break


if len(str(movie_release_year)) != 4:
    while True:
        print(" Please enter a valid year in YYYY format.")
        time.sleep(0.5)
        movie_release_year = int(input("Enter the movie release year (YYYY): "))
        if len(str(movie_release_year)) == 4:
            break

time.sleep(0.3)
print("Calculating...")
time.sleep(1)
print(f" The movie {movie_name} is now {years_released} years old.")           
