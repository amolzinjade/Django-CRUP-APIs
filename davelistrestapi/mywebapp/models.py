from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
from django.db import models
# Create your models here.
CATEGORIES = (
    ('PRIVATE','Private'),
    ('PUBLIC','Public')
)
class listing(models.Model):
    title=models.CharField(max_length=10)
    content=models.CharField(max_length=5000)
    categories=models.CharField(max_length=10,choices=CATEGORIES, default='PUBLIC')
    
    def __str__(self):                                                 # There is double underscore both sides
        return self.title

class Image(models.Model):
    property_id = models.IntegerField(
                    null=False,
                    default=1,
                )
    image = models.ImageField(null=True,blank=True)
    
    def __int__(self):                                                 # There is double underscore both sides
        return self.property_id

class Message(models.Model):
     sender = models.ForeignKey(get_user_model(), related_name="sender",on_delete=models.CASCADE)
     receiver = models.ManyToManyField(get_user_model(), related_name="receiver")
     message = models.CharField(max_length=5000)
     timestamp = models.DateTimeField(auto_now_add=True)
     unread = models.BooleanField(default = True)
     def __str__(self):                                                 # There is double underscore both sides
        return self.message