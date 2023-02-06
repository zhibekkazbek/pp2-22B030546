# Dictionary of movies
movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

# 1

def imdb_score(movie):
    return movie["imdb"] > 5.5
print(imdb_score(movies))

# 2 

def movies_above_55(movies):
    return [movie for movie in movies if movie["imdb"] > 5.5]
print(movies_above_55(movies))

# 3

def category(movies, category):
    return [movie for movie in movies if movie["category"] == category]
print(category(movies, "Romance"))

# 4

def avg_score(movies):
    scores = [movie["imdb"] for movie in movies]
    return sum(scores) / len(scores)
print(avg_score(movies))

# 5

def avg_score_by_category(movies, category):
    scores = [movie["imdb"] for movie in movies if movie["category"] == category]
    avg_score = sum(scores) / len(scores)
    return avg_score
print(avg_score_by_category(movies, "Romance"))