# Generated by Django 4.1.10 on 2023-07-27 06:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("apis_ontology", "0017_remove_person_subject_person_external_link_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="instance",
            name="set_num",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Set 1", "Set 1"),
                    ("Set 2", "Set 2"),
                    ("Set 3", "Set 3"),
                    ("Set 4", "Set 4"),
                ],
                max_length=5,
                null=True,
                verbose_name="Set",
            ),
        ),
    ]
