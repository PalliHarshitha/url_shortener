from django.db import models

# Create your models here.
class ShortURL(models.Model):
    original_url = models.URLField(max_length=700) # input
    short_url = models.CharField(max_length=100)
    #domain.com/tyOp
    time_date_created = models.DateTimeField()

    def _str_(self):
        return self.original_url