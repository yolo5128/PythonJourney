import datetime
import time

favorite_movie = input("What is your favorite movie?: ")
release_year = int(input("What year was the movie released?: "))

current_year = datetime.datetime.now().year
movie_age = current_year - release_year

if not favorite_movie:
    print("You didn't enter a movie title.")
elif not release_year:
    print("You didn't enter a release year.")
else:
    print(f"Your favorite movie is {favorite_movie}, made in {release_year}.")
    
if favorite_movie and release_year:
    time.sleep(1)
    print()
    print(f"{favorite_movie} is now {movie_age} years old!")


