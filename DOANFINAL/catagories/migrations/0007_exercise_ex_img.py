# Generated by Django 3.2.9 on 2021-12-05 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catagories', '0006_remove_exercise_ex_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='ex_img',
            field=models.ImageField(default='static/img/ex/Hiit.png', upload_to='static/img/ex/'),
        ),
    ]
