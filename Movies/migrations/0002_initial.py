# Generated by Django 4.0.6 on 2022-08-14 00:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Movies", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="wanttoseemovie",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="likeformovie",
            name="movie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Movies.tvandmovie"
            ),
        ),
        migrations.AddField(
            model_name="likeformovie",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="likeforcomment_movie",
            name="comment",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Movies.comment"
            ),
        ),
        migrations.AddField(
            model_name="likeforcomment_movie",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="tv_or_movie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="Movies.tvandmovie"
            ),
        ),
        migrations.AddField(
            model_name="comment",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddIndex(
            model_name="comment",
            index=models.Index(
                fields=["user", "tv_or_movie"], name="Movies_comm_user_id_9a38c9_idx"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="comment",
            unique_together={("user", "tv_or_movie")},
        ),
    ]
