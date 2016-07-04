from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

class SaleOrder(models.Model):
    SaleOrderNo = models.CharField(max_length=200),
    OrderDate = models.DateField(),
    PartnerID = models.CharField(max_length=200),
    PartnerInvoice = models.CharField(max_length=1000),
    PartnerShipping = models.CharField(max_length=1000),
    AmountUntaxed = models.DecimalField(max_digits=19, decimal_places=2),
    AmountTax = models.DecimalField(max_digits=19, decimal_places=2),
    AmountTotal = models.DecimalField(max_digits=19, decimal_places = 2),
    Warehouse = models.CharField(max_length=50)
    
    class Meta:
        managed = False

    def __unicode__(self):
        return self.SaleOrderNo

class SaleOrderLine(models.Model):
    SaleOrderNo = models.ForeignKey(SaleOrder, on_delete=models.CASCADE),
    Product = models.CharField(max_length=50),
    Qty = models.IntegerField(),
    Uom = models.CharField(max_length=10),
    Currency = models.CharField(max_length=10),
    PriceUnitAmount = models.DecimalField(max_digits=19, decimal_places=2),
    PriceTaxAmount = models.DecimalField(max_digits=19, decimal_places=2),
    DiscountAmount = models.DecimalField(max_digits=19, decimal_places=2),
    SubTotalAmount = models.DecimalField(max_digits=19, decimal_places=2),
    TotalAmount = models.DecimalField(max_digits=19, decimal_places=2)
    
    class Meta:
        managed = False

    def __unicode__(self):
        return self.Product