from django.shortcuts import render
from movies.models import Movies
from django.http import JsonResponse
import json
import pandas as pd
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Create your views here.


@csrf_exempt
def datagetter(request):
    data = json.loads(request.body)
    o = list(Movies.objects.filter(title__startswith=data["title"]))
    data = []
    count = 0
    for item in o:
        f = {}
        f["Title"] = item.title
        data.append(f)

        count += 1
        if count == 5:
            break
    return JsonResponse({"data": data})


def get_title_from_index(df, index):
    return df[df.index == index]["title"].values[0]


def get_index_from_title(df, title):
    return df[df.title == title]["index"].values[0]


def combine_features(row):
    try:
        return (
            row["keywords"]
            + " "
            + row["cast"]
            + " "
            + row["genres"]
            + " "
            + row["director"]
        )
    except:
        pass


@csrf_exempt
def recommendme(request):
    data = json.loads(request.body)

    df = pd.read_csv("movies/management/commands/movie_dataset.csv")

    features = ["keywords", "cast", "genres", "director"]

    for feature in features:
        df[feature] = df[feature].fillna("")
    df["combined_features"] = df.apply(combine_features, axis=1)

    cv = CountVectorizer()

    count_matrix = cv.fit_transform(df["combined_features"])

    cosine_sim = cosine_similarity(count_matrix)
    movie_user_likes = data["title"]

    movie_index = get_index_from_title(df, movie_user_likes)

    similar_movies = list(enumerate(cosine_sim[movie_index]))

    sorted_similar_movies = sorted(similar_movies, key=lambda x: x[1], reverse=True)

    i = 0
    movies = []
    for element in sorted_similar_movies:
        movies.append(get_title_from_index(df, element[0]))
        i = i + 1
        if i > 6:
            break

    return JsonResponse({"data": movies})


def index(request):
    return render(request, "index.html")
