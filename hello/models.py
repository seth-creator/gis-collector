from django.db import models
#from django.contrib.gis.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField("date created", auto_now_add=True)
    
    
"""class MonOffre(models.Model):
    comm = (('Abobo', 'Abobo'),
                ('Adjamé', 'Adiamé'),
                ('Anyama', 'Anyama'),
                ('Attecoubé', 'Attecoubé'),
                ('Cocody', 'Cocody'),
                ('Koumassi', 'Koumassi'),
                ('Port-bouet', 'Port-bouet'),
                ('Treichville', 'Treichville'),
                ('Songon', 'Songon'),
                ('Yopougon', 'Youpougon'),
                ('Plateau', 'Plateau'),
                ('Marcory', 'Marcory')
                )
    commune = models.CharField('Commune', null = True, max_length = 200, choices = comm)
    contact = models.IntegerField(null =True)
    email = models.EmailField(null=True, max_length = 200)
    agence = models.CharField("Nom de l'agence", max_length = 200, null = True)
    date = models.DateField('Date', null=True)
    geom = models.PointField('Localiser votre bien',blank = True, null = True)"""
    


