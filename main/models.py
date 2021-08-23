from django.db import models

class LOIModel(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    location = models.CharField(max_length=1000)
    address = models.CharField(max_length=1000)
    date = models.CharField(max_length=1000)
    time = models.CharField(max_length=1000)
    advice = models.CharField(max_length=1000)
    added = models.CharField(max_length=1000)
    updated = models.IntegerField(default=1)
    class Meta:
        db_table = 'LOITable'

