from django.utils.dateparse import parse_duration
from django.core.management.base import BaseCommand
from recipes.models import Author, Category, Recipe, Keyword
from kenzieFood.settings import BASE_DIR
from multiprocessing import Process
import time
import csv
import os


class Command(BaseCommand):
    def insert_recipes(self, csvfile):
        # print(csvfile)
        with open(csvfile) as file:
            csv_data = csv.DictReader(file, delimiter=",")
            counter = 0

            recipe_obj_list = []
            keyword_ids = {}
            for row in csv_data:
                author = Author.objects.get_or_create(
                    id=row["AuthorId"], name=row["AuthorName"]
                )[0]
                category = Category.objects.get_or_create(
                    category=row["RecipeCategory"]
                )[0]

                recipe_obj_list.append(
                    Recipe(
                        id=row["RecipeId"],
                        name=row["Name"],
                        date_published=row["DatePublished"],
                        description=row["Description"],
                        calories=float(row["Calories"]),
                        fat_content=float(row["FatContent"]),
                        saturated_fat_content=float(row["SaturatedFatContent"]),
                        cholesterol_content=float(row["CholesterolContent"]),
                        sodium_content=float(row["SodiumContent"]),
                        carbohydrate_content=float(row["CarbohydrateContent"]),
                        fiber_content=float(row["FiberContent"]),
                        sugar_content=float(row["SugarContent"]),
                        protein_content=float(row["ProteinContent"]),
                        recipe_servings=int(float(row["RecipeServings"]))
                        if row["RecipeServings"]
                        else None,
                        cook_time=parse_duration(row["CookTime"]),
                        prep_time=parse_duration(row["PrepTime"]),
                        total_time=parse_duration(row["TotalTime"]),
                        category=category,
                        author=author,
                    )
                )

                keywords = (
                    row["Keywords"]
                    .replace("c(", "")
                    .replace(")", "")
                    .replace('"', "")
                    .split(", ")
                )

                for key in keywords:
                    try:
                        keyword = Keyword.objects.get_or_create(keyword=key)[0]
                    except:
                        keyword = Keyword.objects.filter(keyword=key).first()

                    if keyword.id not in keyword_ids.keys():
                        keyword_ids[keyword.id] = []
                    keyword_ids[keyword.id].append(row["RecipeId"])

                counter += 1

                if counter % 1000 == 0:
                    print(f"Processed {counter} rows of {csvfile}")

            Recipe.objects.bulk_create(recipe_obj_list, ignore_conflicts=True)

            if len(keyword_ids) > 0:
                for k in keyword_ids:
                    try:
                        keyword = Keyword.objects.get(id=k)
                        keyword.recipes.set(keyword_ids[k])
                    except:
                        continue

    def handle(self, *args, **kwargs):
        # é necessário deixar os arquivos CSV no diretório data/recipes/
        recipe_files = [
            os.path.join(BASE_DIR, "data/recipes/") + file
            for file in os.listdir(os.path.join(BASE_DIR, "data/recipes"))
        ]

        for file in recipe_files:
            p = Process(target=self.insert_recipes, args=(file,))
            p.start()
            time.sleep(1.5)
