# Generated by Django 3.2.13 on 2022-07-02 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0003_auto_20220702_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(db_index=True, default=False),
        ),
    ]
