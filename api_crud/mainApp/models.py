from django.db import models

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10,decimal_places=2)
    qty = models.IntegerField()

    # def __str__(self):
    #     return str(self.id)+" "+self.name