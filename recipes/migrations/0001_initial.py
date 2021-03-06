# Generated by Django 3.1.12 on 2021-06-24 03:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('date_published', models.DateTimeField()),
                ('description', models.TextField()),
                ('calories', models.FloatField()),
                ('fat_content', models.FloatField()),
                ('saturated_fat_content', models.FloatField()),
                ('cholesterol_content', models.FloatField()),
                ('sodium_content', models.FloatField()),
                ('carbohydrate_content', models.FloatField()),
                ('fiber_content', models.FloatField()),
                ('sugar_content', models.FloatField()),
                ('protein_content', models.FloatField()),
                ('recipe_servings', models.IntegerField()),
                ('cook_time', models.DurationField()),
                ('pre_time', models.DurationField()),
                ('total_time', models.DurationField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='recipes.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recipes', to='recipes.category')),
            ],
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword', models.CharField(max_length=255)),
                ('recipes', models.ManyToManyField(related_name='keywords', to='recipes.Recipe')),
            ],
        ),
    ]
