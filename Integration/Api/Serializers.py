from rest_framework import serializers
from Api.models import SaleOrder, SaleOrderLine

class SaleOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrder
        fields = ('SaleOrderNo', 'OrderDate', 'PartnerID', 'PartnerInvoice', 'PartnerShipping', 'AmountUntaxed', 'AmountTax', 'AmountTotal', 'Warehouse')

class SaleOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrderLine
        fields = ('Product', 'Qty', 'Uom', 'Currency', 'PriceUnitAmount', 'PriceTaxAmount', 'DiscountAmount', 'SubTotalAmount', 'TotalAmount')