from django.db import models

from accounts.models import User

# Create your models here.
class personal_details(models.Model):

    GENDER = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'), 
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    profile_photo=models.ImageField(upload_to='candidate/profilephoto',default='default.jpg')
    bio=models.CharField(max_length=500,blank=True)
    gender=models.CharField(max_length=50,choices=GENDER,blank=True,null=True)
    dob=models.DateField(blank=True,null=True)
    phone_number=models.CharField(max_length=12)
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    disability_certificate=models.ImageField(upload_to='candidate/disabilityCertificate',default='default.jpg')
    aadhar_number=models.IntegerField()
    aadhar_card=models.ImageField(upload_to='candidate/aadharCard',default='default.jpg')
    disability_type = models.CharField(max_length=100, choices=[
        ('Blindness', 'Blindness'),
        ('Cerebral Palsy', 'Cerebral Palsy'),
        ('Hearing impairment','Hearing impairment'),
        ('Locomotor disability','Locomotor disability'),
        ('Mental illness','Mental illness'),
        ('Haemophilia','Haemophilia'),
        ('Other Disabilities','Other Disabilities')
    ], blank=True, null=True)



class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    highest_qualification=models.CharField(max_length=20)
    specialization=models.CharField(max_length=20)
    institute=models.CharField(max_length=800)
    institute_city=models.CharField(max_length=20,default='')
    institute_state=models.CharField(max_length=20,default='')
    institute_country=models.CharField(max_length=20,default='')
    result=models.CharField(max_length=20,default='')
    start_year=models.DateField();
    end_year=models.DateField();

class Experience(models.Model):
    
    ROLE_CHOICE=(
        (1,'Yes'),
        (2,'No'),
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    Designation=models.CharField(max_length=100)
    Organisation=models.CharField(max_length=100)
    status=models.PositiveSmallIntegerField(choices=ROLE_CHOICE,blank=True,null=True)
    descofjob=models.CharField(max_length=500)
    worked_from = models.DateField()
    worked_till = models.DateField()

class Skills(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    skill=models.CharField(max_length=100)


class keyAchievements(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    achievement=models.CharField(max_length=1000)
    
class Projects(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title=models.CharField(max_length=100)
    link=models.CharField(max_length=100)
    desc=models.CharField(max_length=500)

class Languages(models.Model):
    PROFICIENCY_LEVEL = (
    ('Elementary Proficiency', 'Elementary Proficiency'),
    ('Limited Working Proficiency', 'Limited Working Proficiency'),
    ('Professional Working Proficiency', 'Professional Working Proficiency'), 
    ('Full Professional Proficiency', 'Full Professional Proficiency'), 
    ('Native / Bilingual Proficiency', 'Native / Bilingual Proficiency'), 
    )
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    language=models.CharField(max_length=100)
    proficiency_level=models.CharField(max_length=50,choices=PROFICIENCY_LEVEL,blank=True,null=True)

