# Generated by Django 4.1.10 on 2023-07-06 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("apis_ontology", "0013_delete_role"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="instance",
            name="citation",
        ),
        migrations.AddField(
            model_name="instance",
            name="comments",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="instance",
            name="drepung_number",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Drepung catalogue number",
            ),
        ),
        migrations.AddField(
            model_name="instance",
            name="external_link",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="instance",
            name="num_folios",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Number of folios"
            ),
        ),
        migrations.AddField(
            model_name="instance",
            name="pp_kdsb",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Page numbers in print",
            ),
        ),
        migrations.AddField(
            model_name="instance",
            name="provenance",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Provenance"
            ),
        ),
        migrations.AddField(
            model_name="instance",
            name="sb_text_number",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Number ascribed to item by Tibschol",
            ),
        ),
        migrations.AddField(
            model_name="instance",
            name="set_num",
            field=models.CharField(
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
        migrations.AddField(
            model_name="instance",
            name="signature_letter",
            field=models.CharField(
                blank=True,
                max_length=255,
                null=True,
                verbose_name="Signature letter (category)",
            ),
        ),
        migrations.AddField(
            model_name="instance",
            name="signature_number",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="Signature number"
            ),
        ),
        migrations.AddField(
            model_name="instance",
            name="volume",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]