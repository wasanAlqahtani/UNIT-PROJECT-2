# Generated by Django 5.2.4 on 2025-07-23 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eco', '0002_remove_action_category_action_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.SmallIntegerField(choices=[(1, '👍🏻 Try Harder'), (2, '🎉 Keep Going '), (3, '🤩 Nice Job'), (4, '🥇 Excellent')]),
        ),
    ]
