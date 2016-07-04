from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from Api.models import SaleOrder, SaleOrderLine
from Api.serializers import SaleOrderSerializer, SaleOrderLineSerializer

@api_view(['POST'])
def OrderSyncProcess(request):
    """
    Retreive and process order instance. 
    """
    if request.method == 'POST':
      serializer = SaleOrderSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
