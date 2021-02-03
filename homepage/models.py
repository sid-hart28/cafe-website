from django.db import models

# Create your models here.
class Items(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=10, decimal_places=0)
    availability = models.CharField(max_length=1)
    image = models.ImageField(upload_to='pics')
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'items'

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    quantity = models.IntegerField()
    order_at = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=500)
    phone = models.CharField(max_length=20)
    cus_uname = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'orders'