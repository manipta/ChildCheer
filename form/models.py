from django.db import models
VOL_CHOICES = (
   ('ant', "an Active Ant"),
   ('bird', "a Speedy Sparrow"),
   ('ele', "an Electric Elephant")
)
class formresponse(models.Model):
    name=models.CharField(default=0,max_length=50,null=False,blank=False)
    profession=models.CharField(default=0,max_length=30,null=False,blank=False)
    city=models.CharField(default=0,max_length=50,null=False,blank=False)
    country=models.CharField(default=0,max_length=50,null=False,blank=False)
    contact=models.IntegerField(default=0,null=False,blank=False,unique=True)
    remarks=models.TextField(null=True,blank=True)
    volas=models.CharField(default=0,
        max_length=4, choices=VOL_CHOICES
    )
    # def __str__(self):
    #     return str(self.contact)