from django.db import models

# Create your models here.

class Chatbot(models.Model):
    query = models.CharField(max_length=200)
    response = models.CharField(max_length=200)

    def __str__(self):
        return self.query
