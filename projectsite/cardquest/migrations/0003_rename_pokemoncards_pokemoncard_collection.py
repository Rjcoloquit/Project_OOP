# Generated by Django 4.2.7 on 2023-11-30 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cardquest', '0002_pokemoncards_rename_birthday_trainer_birthdate_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PokemonCards',
            new_name='PokemonCard',
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('collection_date', models.DateField()),
                ('card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cardquest.pokemoncard')),
                ('trainer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cardquest.trainer')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
