from django.db import models

class Blog_entry(models.Model):
    title = models.CharField(max_length=100)
    data = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=240)
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title
