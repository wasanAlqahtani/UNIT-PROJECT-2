# Generated by Django 5.2.4 on 2025-07-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='category',
        ),
        migrations.AddField(
            model_name='action',
            name='location',
            field=models.CharField(choices=[('School', 'School'), ('Home', 'Home'), ('Work', 'Work'), ('Picnic', 'Picnic'), ('Others', 'Others')], default='Others', max_length=1024),
        ),
    ]
