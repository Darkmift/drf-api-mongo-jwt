from djongo import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    synopsis = models.TextField()

    def __str__(self):
        return self.title
