from django.db import models

# Create your models here.

class Movie(models.Model):
    id = models.IntegerField(primary_key=True)
    movieTitle = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    review_content = models.CharField(max_length=100)
    ratings = models.CharField(max_length=2, choices=[('1','1'), ('2', '2'), ('3','3'), ('4', '4'),('5', '5')])
    created_at = models.DateField()
    reviewer_emailId = models.CharField(max_length=100)
    status = models.CharField(max_length=100, choices=[('Published', 'Published'), ('Not Published', 'Not Published')])
    genres = models.CharField(max_length=100, choices=[('Horror', 'Horror'), ('Action', 'Action'), ('SciFi', 'SciFi'), ('Comdey', 'Comedy'), ('Thriller', 'Thriller')])
