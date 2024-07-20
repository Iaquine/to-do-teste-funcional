# Generated by Django 5.0.7 on 2024-07-20 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=200)),
                (
                    "priority",
                    models.CharField(
                        choices=[
                            ("Baixa", "Baixa"),
                            ("Média", "Média"),
                            ("Alta", "Alta"),
                        ],
                        max_length=10,
                    ),
                ),
            ],
        ),
    ]