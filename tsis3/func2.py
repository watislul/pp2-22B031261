# functions2 folder exercises
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


# task 1

def highScoreMov():
    for i in range(len(movies)):
        if movies[i]["imdb"] > 5.5:
            return print(movies[i])


highScoreMov()


# task 2
def highScoreMov():
    for i in range(len(movies)):
        if movies[i]["imdb"] > 5.5:
            movs.append(movies[i])
    print(movs)


movs = []

highScoreMov()


# task 3
def getCateg():
    for i in range(len(movies)):
        if movies[i]["category"] == "Thriller":
            print(movies[i])


getCateg()


# task 4

def imdbAvg():
    for i in movies:
        avg = sum(j["imdb"] for j in movies) / len(movies)
    print(avg)


avg = 0
imdbAvg()


# task 5

def imdbCatAvg():
    for i in range(len(movies)):
        if movies[i]["category"] == cat:
            movs.append(movies[i])
    avg = sum(j["imdb"] for j in movs) / len(movs)
    print(avg)


cat = input()
movs = []
avg = 0
imdbCatAvg()