# Generated by Django 3.1.14 on 2022-02-15 06:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apis_metainfo', '0002_auto_20220201_1241'),
        ('apis_entities', '0001_initial'),
        ('apis_labels', '0002_auto_20220201_1241'),
        ('apis_relations', '0002_property_property_class_uri'),
        ('apis_ontology', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xml_File',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_entities.tempentityclass')),
                ('file_path', models.CharField(blank=True, max_length=1024, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_entities.tempentityclass',),
        ),
        migrations.AddField(
            model_name='f10_person',
            name='gnd_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='f1_work',
            name='gnd_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='XmlFile',
        ),
    ]
