# Generated by Django 3.1.14 on 2022-02-01 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('apis_entities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('tempentityclass_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_entities.tempentityclass')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_entities.tempentityclass',),
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_ontology.resource')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_ontology.resource',),
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_ontology.resource')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_ontology.resource',),
        ),
        migrations.CreateModel(
            name='Identifier',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_ontology.resource')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_ontology.resource',),
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_ontology.resource')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_ontology.resource',),
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_ontology.resource')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_ontology.resource',),
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_ontology.resource')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_ontology.resource',),
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('resource_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_ontology.resource')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_ontology.resource',),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('agent_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apis_ontology.agent')),
            ],
            options={
                'abstract': False,
            },
            bases=('apis_ontology.agent',),
        ),
    ]