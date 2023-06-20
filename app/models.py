from django.db import models

# Create your models here.
class Country(models.Model):
    country_name=models.CharField(max_length=100, primary_key=True)

    def __str__(self):
        return self.country_name

class State(models.Model):
    country_name=models.ForeignKey(Country, on_delete=models.CASCADE)
    state_name=models.CharField(max_length=100)
     
    def __str__(self):
        return self.state_name

# class AccessRecords(models.Model):
#     name=models.ForeignKey(Webpage, on_delete=models.CASCADE)
#     date=models.DateField()
#     author=models.CharField(max_length=100)


#     def __str__(self):
#         return self.author        