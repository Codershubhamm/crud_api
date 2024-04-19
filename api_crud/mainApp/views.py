from django.shortcuts import render
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view


@api_view(['GET'])
def products(request):
    product_obj = Product.objects.all()
    serializer = ProductSerializer(product_obj,many=True)
    print(serializer)
    return Response({'status':'200 Response Received','New_Products':serializer.data})


@api_view(['GET'])
def s_products(request,id):
    product_obj = Product.objects.get(id=id)
    moralizer = ProductSerializer(product_obj)
    return Response({'status':'200 Response Received','ew_Products':moralizer.data})

@api_view(['POST'])
def recproducts(request):
    moralizer = ProductSerializer(data=request.data)
    if not moralizer.is_valid():
        return Response({'error':moralizer.errors,"My_message":"Sorry data invalid"})
    else:
        moralizer.save()
    return Response({'status':'Input Received','ew_Products':moralizer.data})

# @api_view(['PUT'])
# def patproducts(request,id):
#     try:
#         product_obj = Product.objects.get(id=id)
#         moralizer = ProductSerializer(product_obj ,data=request.data,partial=True)
#         if not moralizer.is_valid():
#             return Response({'error':moralizer.errors,"My_message":"Update data invalid"})
#         else:
#             moralizer.save()
#             return Response({'status':'Input Received','ew_Products':moralizer.data})
#     except:
#         return Response({"My_message":"Update id invalid"})

@api_view(['PUT','PATCH'])
def patproducts(request,id):
    product_obj = Product.objects.get(id=id)
    moralizer = ProductSerializer(product_obj ,data=request.data,partial=True)
    if not moralizer.is_valid():
        return Response({'error':moralizer.errors,"My_message":"Update data invalid"})
    else:
        moralizer.save()
    return Response({'status':'Input Received','ew_Products':moralizer.data})

@api_view(['DELETE'])
def deletep(request,id):
    product_obj = Product.objects.get(id=id)
    serializers = ProductSerializer(product_obj)
    product_obj.delete()
    return Response({'NProduct':serializers.data,'Message':"Data Deleted"})
