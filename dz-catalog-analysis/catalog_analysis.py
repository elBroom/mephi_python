import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, 
     "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]


def average_rating(movies):
    return round(sum(m["rating"] for m in movies)/len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    return (
        max(current_year-m["year"] for m in movies), 
        min(current_year-m["year"] for m in movies), 
        math.ceil(sum(current_year-m["year"]  for m in movies)/len(movies))
    )


def duration_in_hours(minutes):
    return f'{minutes//60}ч {minutes%60}м'


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    match year:
       case n if n > 2020:
           return "новые"
       case n if 2015 <= n <= 2020:
           return "недавние"
       case _:
           return "старые"


def get_no_comedy(movie):
    for move in movies:
        if "comedy" in move["genres"]:
            continue
        print(move["title"])


def find_masterpiece(movie):
    i = 0
    while i < len(movies):
        if movies[i]["rating"] >= 9:
            print(movies[i]["title"])
            break
        i += 1
    else:
        print("Шедевров не найдено")


def count_long_movies(movies, threshold=120):
    cnt = 0
    for move in movies:
        if move["duration_min"] > threshold:
           cnt += 1
    return cnt


def normalize_title(title):
    return " ".join(word[0].upper() + word[1:] for word in title.split())


def make_slug(title):
    return title.lower().replace(" ", "-")


def format_report_line(movie):
    duration = duration_in_hours(movie["duration_min"])
    return (
        f'"{movie["title"]}" ({movie["year"]}) — {movie["rating"]}/10, '+
        f'{duration}, жанры: {", ".join(sorted(movie["genres"]))}'
    )

def titles_sorted_by_rating(movies):
    return [m["title"] for m in sorted(movies, key=lambda m: m["rating"], reverse=True)]


def top_n_by_rating(movies, n=3):
    return [
        (m["title"], m["rating"]) 
        for m in sorted(movies, key=lambda m: m["rating"], reverse=True)
    ][:n]


def count_by_genre(movies):
    genres = {}
    for m in movies:
        for g in m["genres"]:
            genres[g] = genres.get(g, 0) + 1
    return genres


def actor_filmography(movies):
    actors = {}
    for m in movies:
        for a in m["actors"]:
            actors[a] = actors.get(a, []) + [m["title"]]
    return actors


def get_high_move(movies):
    avg = average_rating(movies)
    return {m["title"]: m["rating"] for m in movies if m["rating"] > avg}


def main():
    print("main")


if __name__ == "__main__":
    main()
