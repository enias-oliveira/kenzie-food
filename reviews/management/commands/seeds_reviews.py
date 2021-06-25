import csv
from django.core.management.base import BaseCommand
from recipes.models import Author, Recipe
from reviews.models import Review
from kenzieFood.settings import BASE_DIR
from multiprocessing import Process
import time
import os


class Command(BaseCommand):
    def insert_reviews(self, csvfile):
        # print(csvfile)
        with open(csvfile) as file:
            csv_data = csv.DictReader(file, delimiter=",")
            counter = 0

            review_obj_list = []
            for row in csv_data:

                try:
                    author = Author.objects.get_or_create(
                        id=row["AuthorId"],
                        name=row["AuthorName"],
                    )[0]
                    recipe = Recipe.objects.get(id=row["RecipeId"])
                    review_obj_list.append(
                        Review(
                            review=row["Review"],
                            rating=row["Rating"],
                            date_submitted=row["DateSubmitted"],
                            author=author,
                            recipe=recipe,
                        )
                    )

                except:
                    continue

                counter += 1

                if counter % 1000 == 0:
                    print(f"Processed {counter} rows of {csvfile}")

            Review.objects.bulk_create(review_obj_list, ignore_conflicts=True)

    def handle(self, *args, **kwargs):
        # é necessário deixar os arquivos CSV no diretório data/reviews/
        review_files = [
            os.path.join(BASE_DIR, "data/reviews/") + file
            for file in os.listdir(os.path.join(BASE_DIR, "data/reviews"))
        ]

        for file in review_files:
            p = Process(target=self.insert_reviews, args=(file,))
            p.start()
            time.sleep(1.5)
