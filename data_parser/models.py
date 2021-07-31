from django.db import models


class PokeFileDownLoadModel(models.Model):
    file_name = models.CharField(max_length=250)
    url = models.URLField(max_length = 250)
    date = models.DateField(auto_now_add=True)
