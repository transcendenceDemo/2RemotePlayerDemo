# Generated by Django 3.2.25 on 2024-09-27 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player1_score', models.IntegerField(default=0)),
                ('player2_score', models.IntegerField(default=0)),
                ('ball_x', models.FloatField(default=0.5)),
                ('ball_y', models.FloatField(default=0.5)),
                ('ball_dx', models.FloatField(default=0.005)),
                ('ball_dy', models.FloatField(default=0.005)),
                ('paddle1_y', models.FloatField(default=0.5)),
                ('paddle2_y', models.FloatField(default=0.5)),
            ],
        ),
    ]
