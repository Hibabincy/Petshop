from django.db import models

# Create your models here.
class Reg_tbl(models.Model):
    fnm = models.CharField(max_length=25)
    mob = models.IntegerField()
    eml = models.EmailField()
    psw = models.CharField(max_length=16)
    cpsw = models.CharField(max_length=16)

class pet_tbl(models.Model):
    pnm=models.CharField(max_length=25)
    pim=models.FileField(upload_to='pic')
    prc=models.IntegerField()
    des=models.TextField()

class cart_tbl(models.Model):
    customer=models.ForeignKey(Reg_tbl,on_delete=models.CASCADE) 
    product=models.ForeignKey(pet_tbl,on_delete=models.CASCADE)
    qty=models.PositiveIntegerField(default=1)


