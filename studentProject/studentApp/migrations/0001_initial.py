# Generated by Django 5.0.1 on 2024-01-28 08:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="STUDENTS",
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
                ("s_reg", models.CharField(max_length=15)),
                ("s_name", models.CharField(max_length=15)),
                ("s_email", models.CharField(max_length=30)),
                ("s_department", models.CharField(max_length=15)),
                ("s_semester", models.CharField(max_length=15)),
                ("s_attendance", models.CharField(max_length=15)),
                ("s_cgpa", models.CharField(max_length=15)),
            ],
        ),
    ]
