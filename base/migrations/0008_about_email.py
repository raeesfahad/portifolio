# Generated by Django 4.0.6 on 2022-07-26 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_remove_me_tagline_me_tagline'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='email',
            field=models.EmailField(default='ifahadullahkhan@gamil.com', max_length=254),
        ),
    ]
