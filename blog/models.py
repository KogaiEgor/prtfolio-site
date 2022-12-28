from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=60)
    date = models.DateField(auto_now=True)
    description = models.TextField(max_length=3000)

    def __str__(self):
        return self.title

