# Generated by Django 3.2.5 on 2021-09-18 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_selected_paper_reviewer'),
    ]

    operations = [
        migrations.CreateModel(
            name='reviewed_papers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Topic', models.CharField(max_length=20)),
                ('Url', models.URLField()),
                ('Department', models.CharField(max_length=20)),
                ('emaiid', models.CharField(max_length=50)),
            ],
        ),
    ]