# Generated by Django 4.0.6 on 2022-08-18 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Movies", "0004_rename_likeforcomment_movie_likeforcomment_and_more"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="comment",
            constraint=models.CheckConstraint(
                check=models.Q(("stars__gte", 0.0), ("stars__lte", 10.0)),
                name="cooment_stars_range",
            ),
        ),
    ]
