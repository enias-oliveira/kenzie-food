# Generated by Django 3.1.12 on 2021-06-30 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20210624_0404'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipe',
            options={'ordering': ['name']},
        ),
        migrations.AddIndex(
            model_name='recipe',
            index=models.Index(fields=['name'], name='recipes_rec_name_891f25_idx'),
        ),
    ]
