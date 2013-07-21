from django.db import models

# Create your models here.

class Constituency(models.Model):
    
    
    name = models.TextField()
    
    
    
    def __unicode__(self):
        
        return self.name
    


class User(models.Model):
    name = models.TextField()

class Election(models.Model):
    
    constituency = models.ForeignKey(Constituency)
    name = models.TextField()
    end_date = models.DateTimeField()
    
    moderators = models.ManyToManyField(User)
    
    def __unicode__(self):
        
        return self.name
