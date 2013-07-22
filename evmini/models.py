from django.db import models

# Create your models here.


class ParentConstituency(models.Model):
    state_name = models.CharField(max_length=30)
    city_name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.state_name + " " + city_name

        
class Constituency(models.Model):
    name = models.CharField(max_length=75)
    description = models.TextField()
    parentconstituency = models.ForeignKey(ParentConstituency)
    
    def __unicode__(self):
        return self.name

    
class Election(models.Model):
    constituency = models.ForeignKey(Constituency)
    name = models.CharField(max_length=50)
    description = models.TextField()
    first_voting_day = models.DateTimeField()
    last_voting_day = models.DateTimeField()
        
    def __unicode__(self):
        return self.name

        
class Office(models.Model):
    election = models.ForeignKey(Election)
    name = models.CharField(max_length=30)
    description = models.TextField()
    term_start = models.DateTimeField()
    term_end = models.DateTimeField()

    def __unicode__(self):
        return self.name
        
        
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    description = models.TextField()
    # (not sure how to do this...) image = models.ImageField()
    private_email = models.EmailField()
    # public_email = models.EmailField()
    # twitter_name = models.CharField()
    # facebook_page = models.CharField()
    # linkedin_page = models.CharField()
    # personal_homepage = models.CharField()
    

    def __unicode__(self):
        return self.first_name + " " + self.last_name        
    
    
class Candidate(models.Model):
    user = models.ForeignKey(User)
    # elections = models.ManyToManyField(Electin) (do we need this? or would the offices.id suffice?)
    offices = models.ManyToManyField(Office)
    
    def __unicode__(self):
        return self.user

        
class Moderator(models.Model):
    user = models.ForeignKey(User)
    elections = models.ManyToManyField(Election)
    # do we need offices here? or can those be accessed through elections variable above?
    
    def __unicode__(self):
        return self.user
        

class Administrator(models.Model):
    user = models.ForeignKey(User)
    constituencies = models.ManyToManyField(Constituency)
    # do we need elections and offices here?
    
    def __unicode__(self):
        return self.user
        
        
class Vote(models.Model):
    # I really don't understand how the Votes and Comments classes should be setup here...
    user = models.ForeignKey(User)
    candidate = models.ForeignKey(Candidate)
    moderator = models.ForeignKey(Moderator)
    administator = models.ForeignKey(Administrator)
    
    def __unicode__(self):
        return self.user

        
class Comment(models.Model):
    # Uh...hmmm...how?...have no idea when ForeignKey or ManyToManyFields...
    body = models.TextField()
    created = models.DateTimeField()
    user = models.ForeignKey(User)
    candidate = models.ForeignKey(Candidate)
    moderator = models.ForeignKey(Moderator)
    adminstrator = models.ForeignKey(Administrator)
    
    def __unicode__(self):
        return self.body