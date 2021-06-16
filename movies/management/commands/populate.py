from django.core.management.base import BaseCommand, CommandError
from movies.models import Movies
import pandas as pd


class Command(BaseCommand):
    def handle(self, *args, **options):

        data = pd.read_csv("movies/management/commands/movie_dataset.csv")

        features = ["title", "keywords", "cast", "genres", "director"]

        for feature in features:
            data[feature] = data[feature].fillna("")

        data = data[features]

        for i in range(len(data["title"])):
            title = data["title"][i]
            keywords = data["keywords"][i]
            cast = data["cast"][i]
            genre = data["genres"][i]
            director = data["director"][i]

            a = Movies(
                title=title,
                keywords=keywords,
                cast=cast,
                genre=genre,
                director=director,
            )
            a.save()
