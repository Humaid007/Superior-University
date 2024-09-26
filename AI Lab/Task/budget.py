movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]

add_more_movies = input("Do you want to add more movies? (yes/no): ")
if add_more_movies.lower() == "yes":
    num_movies_to_add = int(input("How many movies do you want to add?: "))
    for i in range(num_movies_to_add):
        movie_name = input("Enter the movie name: ")
        movie_budget = int(input("Enter the movie budget: "))
        movies.append((movie_name, movie_budget))

total_budget = sum(budget for _, budget in movies)

average_budget = total_budget / len(movies)

print(f"Average budget: ${average_budget:.2f}")

high_budget_count = 0

for movie, budget in movies:
    if budget > average_budget:
        high_budget_count += 1
        print(f"{movie} has a budget of ${budget:.2f}, which is ${budget - average_budget:.2f} higher than the average.")

print(f"{high_budget_count} movies spent more than the average budget.")