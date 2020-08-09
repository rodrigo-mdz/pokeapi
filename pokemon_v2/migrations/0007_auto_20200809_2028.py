# Generated by Django 2.1.11 on 2020-08-09 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pokemon_v2", "0006_pokemonspecies_is_legendary"),
    ]

    operations = [
        migrations.AddField(
            model_name="pokemonspecies",
            name="is_mythical",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="pokemonspecies",
            name="is_ultra_beast",
            field=models.BooleanField(default=False),
        ),
    ]
