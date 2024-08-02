# Generated by Django 5.0.7 on 2024-08-02 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('movieTitle', models.CharField(max_length=100)),
                ('director', models.CharField(max_length=100)),
                ('review_content', models.CharField(max_length=100)),
                ('ratings', models.IntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])),
                ('created_at', models.DateField()),
                ('reviewer_emailId', models.EmailField(max_length=254)),
                ('status', models.CharField(choices=[('Published', 'Published'), ('Not Published', 'Not Published')], max_length=100)),
                ('genres', models.CharField(choices=[('Horror', 'Horror'), ('Action', 'Action'), ('SciFi', 'SciFi'), ('Comdey', 'Comedy'), ('Thriller', 'Thriller')], max_length=100)),
            ],
        ),
    ]
