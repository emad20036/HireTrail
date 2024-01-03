from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _


class Person(models.Model): 
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, blank=True, null=True, unique=True)
    fname=models.CharField(max_length=50, blank=True, null=True)
    lname=models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)

    def __str__(self):
        return f"{self.fname} - {self.lname}" 
@receiver(post_save, sender=User)
def create_person_for_user(sender, instance, created, **kwargs):
    if created:
        # Create a Person instance for the new User and populate fields
        person = Person.objects.create(
            user=instance,
            username=instance.username,
            fname=instance.first_name,
            lname=instance.last_name,
            email=instance.email
        )

# Connect the signal
post_save.connect(create_person_for_user, sender=User)




class Job(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('Interview', 'Interview'),
        ('declined', 'declined'),
    )

    JOB_TYPE=(
        ('full-time', 'full-time'),
        ('part-time', 'part-time'),
        ('internship', 'internship'),
    )
    person = models.ForeignKey(Person, null=True, on_delete=models.SET_NULL)
    company = models.CharField(max_length=190, null=True)
    position = models.CharField(max_length=190, null=True)
    status = models.CharField(max_length=190, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    job_location = models.CharField(max_length=190, null=True)
    job_type = models.CharField(max_length=190, null=True, choices=JOB_TYPE)


    def __str__(self):
        return f"{self.company} - {self.position}" 