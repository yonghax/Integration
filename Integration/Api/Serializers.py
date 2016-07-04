from rest_framework import serializers
from Api.models import SaleOrder, SaleOrderLine

class SaleOrderLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrderLine
        fields = ('Product', 'Qty', 'Uom', 'Currency', 'PriceUnitAmount', 'PriceTaxAmount', 'DiscountAmount', 'SubTotalAmount', 'TotalAmount')

class SaleOrderSerializer(serializers.ModelSerializer):
    SalesOrderLines = SaleOrderLineSerializer(many=True, read_only=True)
    class Meta:
        model = SaleOrder
        fields = ('SaleOrderNo', 'OrderDate', 'PartnerID', 'PartnerInvoice', 'PartnerShipping', 'AmountUntaxed', 'AmountTax', 'AmountTotal', 'Warehouse', 'SalesOrderLines')